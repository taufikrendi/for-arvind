import requests, logging, uuid, json, threading

from confluent_kafka.avro import AvroProducer

from kafka_connector import prod_conf, on_delivery

from account.models import AccountMemberVerifyStatus
from account.serialize_avro.get_score import get_score_schema, GetScore

logger = logging.getLogger(__name__)


def nodeflux_produce_get_result():
    check_selfie_score = AccountMemberVerifyStatus.objects.using('default_slave').filter(
        account_member_verify_status_dukcapil_score__isnull=True
    ).extra(
        select={'account_profile_identification_number': 'account_accountprofile.account_profile_identification_number',
                'account_profile_selfie': 'account_accountprofile.account_profile_selfie'},
        tables=['account_accountprofile'],
        where=['account_accountprofile.account_profile_user_related='
               'account_accountmemberverifystatus.account_member_verify_status_user_related']
    ).values('account_profile_identification_number', 'account_profile_selfie')[:1]

    if check_selfie_score:
        for i in range(0, 2):
            the_headers = {'Authorization': 'NODEFLUX-HMAC-SHA256'
                                            'Credential=2JU393GT82FJR97T1HGW91CRG/20210624/nodeflux.api.v1beta1.ImageAnalytic/StreamImageAnalytic, '
                                            'SignedHeaders=x-nodeflux-timestamp, Signature=59181286b93b8b80b0e87257a7d3a7e5bfe2d11a7b3dcdb314b02e22734e95b7',
                           'x-nodeflux-timestamp': '20210624T060005Z',
                           'Content-Type': 'application/json'}
            send_data = {
               "additional_params": {
                   "nik": check_selfie_score[i]['account_profile_identification_number'],
                   "transaction_id": str(uuid.uuid4()),
                   "transaction_source": "server-01"
               },
               "images": [
                   check_selfie_score[i]['account_profile_selfie'],
               ]
            }[i]
            results = requests.post('https://api.cloud.nodeflux.io/v1/analytics/dukcapil-validation',
                                   data=json.dumps(send_data[i]),
                                   headers=the_headers).json()
            consume_results = requests.get(
                'https://api.cloud.nodeflux.io/v1/jobs/{}'.format(results['job']['id']),
                headers=the_headers).json()
            producer = AvroProducer(prod_conf, default_value_schema=get_score_schema)
            logger.info("Start Producing user records to topic {}".format('scheduled_get_score'))
            record = GetScore()
            record.nik = check_selfie_score[i]['account_profile_identification_number']
            record.id = results['job']['id']
            record.status = results['job']['result']['status']
            record.analytic_type = results['job']['result']['analytic_type']
            record.message = results['message']
            record.ok = results['ok']
            record.consume_jobs_id = consume_results['job']['id']
            record.consume_status_status = consume_results['job']['result']['status']
            record.consume_status_analytic_type = consume_results['job']['result']['analytic_type']
            record.consume_status_message = consume_results['message']
            record.consume_status_ok = consume_results['message']
            record.consume_status_similarity = consume_results['job']['result']['result'][0]['face_match']['similarity']
            producer.poll(0.1)
            producer.produce(topic='scheduled_get_score', value=record.to_dict(),
                             partition=0, callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
            threading.Thread(target=producer.flush())
            logger.info("Success Producing user {} records to topic {}".format(record.nik, 'scheduled_get_score'))
    else:
        pass