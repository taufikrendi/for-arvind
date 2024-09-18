from confluent_kafka import avro

create_funds_raise_schema = avro.loads("""
    {
      "doc": "member create funds raise value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member code",
          "name": "code",
          "type": "string"
        },
        {
          "doc": "Member amount",
          "name": "amount",
          "type": "float"
        }, 
        {
          "doc": "Member get saving",
          "name": "get_saving",
          "type": "string"
        },
        {
          "doc": "Member from saving amount",
          "name": "from_saving_amount",
          "type": "float"
        },
        {
          "doc": "Member unique code",
          "name": "unique_code",
          "type": "int"
        },
        {
          "doc": "Member Transaction Status",
          "name": "payment_with",
          "type": "string"
        }
      ],
      "name": "memberCreateFundsRaise",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")