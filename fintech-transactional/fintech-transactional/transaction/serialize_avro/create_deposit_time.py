from confluent_kafka import avro

create_deposit_time_schema = avro.loads("""
    {
      "doc": "member create transaction value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member ID Deposit",
          "name": "product_type",
          "type": "string"
        },
        {
          "doc": "Member amount",
          "name": "amount",
          "type": "int"
        }, 
        {
          "doc": "Member period_base",
          "name": "period_base",
          "type": "int"
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
