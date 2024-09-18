from confluent_kafka import avro

selfie_filled_schema = avro.loads("""
    {
      "doc": "member Selfie filled value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member Ip Address",
          "name": "selfie",
          "type": "string"
        }, 
        {
          "doc": "Member Last Pwd",
          "name": "selfie_ektp",
          "type": "string"
        }, 
        {
          "doc": "Member Last Pwd",
          "name": "ektp",
          "type": "string"
        }, 
        {
          "doc": "Member Last Pwd",
          "name": "enpwp",
          "type": "string"
        }
      ],
      "name": "memberSelfieFilled",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")