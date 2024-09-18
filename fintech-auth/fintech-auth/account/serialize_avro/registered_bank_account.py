from confluent_kafka import avro

registered_bank_account_schema = avro.loads("""
    {
      "doc": "member register bank account value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member bank code",
          "name": "holder_bank_code",
          "type": "string"
        },
        {
          "doc": "Member holder number",
          "name": "holder_number",
          "type": "string"
        }, 
        {
          "doc": "Member holder name",
          "name": "holder_name",
          "type": "string"
        }
      ],
      "name": "memberRegisteredBankAccount",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")