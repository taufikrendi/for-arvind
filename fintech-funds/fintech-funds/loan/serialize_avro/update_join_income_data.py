from confluent_kafka import avro

update_join_income_schema = avro.loads("""
    {
      "doc": "member update join income schema value",
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
          "doc": "Member join_income",
          "name": "join_income",
          "type": "string"
        }, 
        {
          "doc": "Member company_name",
          "name": "company_name",
          "type": "string"
        },
        {
          "doc": "Member company_phone",
          "name": "company_phone",
          "type": "string"
        },
        {
          "doc": "Member company_address_prov",
          "name": "company_address_prov",
          "type": "string"
        },
        {
          "doc": "Member company_address_district",
          "name": "company_address_district",
          "type": "string"
        },
        {
          "doc": "Member company_address_sub_district",
          "name": "company_address_sub_district",
          "type": "string"
        },
        {
          "doc": "Member company_postal_code",
          "name": "company_postal_code",
          "type": "string"
        },
        {
          "doc": "Member company_establish_from",
          "name": "company_establish_from",
          "type": "string"
        },
        {
          "doc": "Member company_category",
          "name": "company_category",
          "type": "string"
        },
        {
          "doc": "Member job_started_date",
          "name": "job_started_date",
          "type": "string"
        },
        {
          "doc": "Member job_status",
          "name": "job_status",
          "type": "string"
        },
        {
          "doc": "Member job_evident",
          "name": "job_evident",
          "type": "string"
        },
        {
          "doc": "Member salary",
          "name": "salary",
          "type": "float"
        },
        {
          "doc": "Member placement",
          "name": "placement",
          "type": "string"
        }
      ],
      "name": "memberUpdateJoinIncome",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")