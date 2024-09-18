from confluent_kafka import avro

registration_schema = avro.loads("""
    {
      "doc": "member registrations value",
      "fields": [
        {
          "doc": "Member E-Mail",
          "name": "email",
          "type": "string"
        },
        {
          "doc": "phone_number",
          "name": "phone_number",
          "type": "string"
        },
        {
          "doc": "Full Name",
          "name": "first_name",
          "type": "string"
        },
        {
          "doc": "password hash",
          "name": "password",
          "type": "string"
        },
        {
          "doc": "member agreement",
          "name": "agreement",
          "type": "string"
        }
      ],
      "name": "memberRegistrations",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")