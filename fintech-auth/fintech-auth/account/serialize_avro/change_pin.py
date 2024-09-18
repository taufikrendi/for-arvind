from confluent_kafka import avro

change_pin_schema = avro.loads("""
    {
      "doc": "member change pin value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member Ip Address",
          "name": "ip",
          "type": "string"
        }, 
        {
          "doc": "Member Last Pwd",
          "name": "pin",
          "type": "string"
        },
        {
          "doc": "Member New Pwd",
          "name": "new_pin",
          "type": "string"
        }
      ],
      "name": "memberChangePassword",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")