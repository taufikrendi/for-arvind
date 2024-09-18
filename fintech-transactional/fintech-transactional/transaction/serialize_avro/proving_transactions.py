from confluent_kafka import avro

proving_transactions_schema = avro.loads("""
    {
      "doc": "member proving transaction value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member trans id",
          "name": "trans_id",
          "type": "string"
        },
        {
          "doc": "Member image proving",
          "name": "image",
          "type": "string"
        }
      ],
      "name": "memberProvingTransaction",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")