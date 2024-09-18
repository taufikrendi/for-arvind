from confluent_kafka import avro

create_loan_application_schema = avro.loads("""
    {
      "doc": "member create submission schema value",
      "fields": [
        {
          "doc": "Member email",
          "name": "email",
          "type": "string"
        },
        {
          "doc": "Member type_usage",
          "name": "type_usage",
          "type": "string"
        }, 
        {
          "doc": "Member amount",
          "name": "amount",
          "type": "float"
        },
        {
          "doc": "Member installment_month",
          "name": "installment_month",
          "type": "int"
        },
        {
          "doc": "Member reason",
          "name": "reason",
          "type": "string"
        },
        {
          "doc": "Member collateral",
          "name": "collateral",
          "type": "string"
        },
        {
          "doc": "Member proving_collateral",
          "name": "proving_collateral",
          "type": "string"
        },
        {
          "doc": "Member url",
          "name": "url",
          "type": "string"
        }
      ],
      "name": "memberCreateSubmission",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")