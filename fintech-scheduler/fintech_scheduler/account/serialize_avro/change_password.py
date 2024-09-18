from confluent_kafka import avro

change_password_schema = avro.loads("""
    {
      "doc": "member change password value",
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
          "doc": "Member New Pwd",
          "name": "new_pwd",
          "type": "string"
        }
      ],
      "name": "memberChangePassword",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")