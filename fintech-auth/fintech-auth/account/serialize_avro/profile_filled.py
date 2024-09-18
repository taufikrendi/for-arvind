from confluent_kafka import avro

account_profile_schema = avro.loads("""
    {
      "doc": "member profile update value",
      "fields": [
        {
          "doc": "Member username",
          "name": "username",
          "type": "string"
        },
        {
          "doc": "Member identity",
          "name": "ektp_number",
          "type": "string"
        },
        {
          "doc": "Member tax number",
          "name": "npwp_number",
          "type": "string"
        },
        {
          "doc": "Member dob",
          "name": "dob",
          "type": "string"
        }, 
        {
          "doc": "Member pob",
          "name": "pob",
          "type": "int"
        },
        {
          "doc": "Member sex",
          "name": "sex",
          "type": "string"
        },
        {
          "doc": "Member address",
          "name": "address",
          "type": "string"
        },
        {
          "doc": "Member province",
          "name": "province",
          "type": "int"
        },
        {
          "doc": "Member district",
          "name": "district",
          "type": "int"
        },
        {
          "doc": "Member sub_district",
          "name": "sub_district",
          "type": "int"
        }
      ],
      "name": "memberProfile",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")