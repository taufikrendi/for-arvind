from confluent_kafka import avro

create_transactions_schema = avro.loads("""
    {
      "doc": "member create transaction value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member Unique Code",
          "name": "unique_code",
          "type": "int"
        },
        {
          "doc": "Member Amount",
          "name": "amount",
          "type": "float"
        },
        {
          "doc": "Member Transaction Status",
          "name": "payment_with",
          "type": "string"
        }
      ],
      "name": "memberCreateTransaction",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")