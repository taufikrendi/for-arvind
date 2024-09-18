from confluent_kafka import avro

get_score_schema = avro.loads("""
    {
      "doc": "EKYC Score value",
      "fields": [
        {
          "doc": "EKYC Score nik",
          "name": "nik",
          "type": "string"
        },
        {
          "doc": "EKYC Score id",
          "name": "id",
          "type": "string"
        }, 
        {
          "doc": "EKYC Score status",
          "name": "status",
          "type": "string"
        }, 
        {
          "doc": "EKYC Score analytic_type",
          "name": "analytic_type",
          "type": "string"
        },
        {
          "doc": "EKYC Score message",
          "name": "message",
          "type": "string"
        },
        {
          "doc": "EKYC Score ok",
          "name": "ok",
          "type": "boolean"
        },
        {
          "doc": "EKYC Score consume_jobs_id",
          "name": "consume_jobs_id",
          "type": "string"
        },
        {
          "doc": "EKYC Score consume_status_status",
          "name": "consume_status_status",
          "type": "string"
        },
        {
          "doc": "EKYC Score consume_status_analytic_type",
          "name": "consume_status_analytic_type",
          "type": "string"
        },
        {
          "doc": "EKYC Score consume_status_message",
          "name": "consume_status_message",
          "type": "string"
        },
        {
          "doc": "EKYC Score consume_status_ok",
          "name": "consume_status_ok",
          "type": "boolean"
        },
        {
          "doc": "EKYC Score consume_status_similarity",
          "name": "consume_status_similarity",
          "type": "float"
        }
      ],
      "name": "memberEKYCScore",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")