from confluent_kafka import avro

forgot_password_schema = avro.loads("""
    {
      "doc": "member forgot password value",
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
        }
      ],
      "name": "memberForgotPassword",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")