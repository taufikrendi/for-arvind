from confluent_kafka import avro

update_spouse_data_schema = avro.loads("""
    {
      "doc": "member update spouse data schema value",
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
          "doc": "Member guarantor",
          "name": "guarantor",
          "type": "string"
        },
        {
          "doc": "Member full_name",
          "name": "full_name",
          "type": "string"
        },
        {
          "doc": "Member status",
          "name": "status",
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
          "type": "string"
        },
        {
          "doc": "Member district",
          "name": "district",
          "type": "string"
        },
        {
          "doc": "Member sub_district",
          "name": "sub_district",
          "type": "string"
        },
        {
          "doc": "Member postal_code",
          "name": "postal_code",
          "type": "string"
        },
        {
          "doc": "Member phone_number",
          "name": "phone_number",
          "type": "string"
        }
      ],
      "name": "memberUpdateSpouseData",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")