from confluent_kafka import avro

update_spouse_selfie_data_schema = avro.loads("""
    {
      "doc": "member update spouse selfie data schema value",
      "fields": [
        {
          "doc": "Member email",
          "name": "email",
          "type": "string"
        },
        {
          "doc": "Member code",
          "name": "code",
          "type": "string"
        },
        {
          "doc": "Member selfie",
          "name": "selfie",
          "type": "string"
        }, 
        {
          "doc": "Member selfie_eidentity",
          "name": "selfie_eidentity",
          "type": "string"
        },
        {
          "doc": "Member eidentity",
          "name": "eidentity",
          "type": "string"
        },
        {
          "doc": "Member enpwp",
          "name": "enpwp",
          "type": "string"
        },
        {
          "doc": "Member family_card",
          "name": "family_card",
          "type": "string"
        },
        {
          "doc": "Member marriage_certificate",
          "name": "marriage_certificate",
          "type": "string"
        }
      ],
      "name": "memberUpdateSpouseSelfieData",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")