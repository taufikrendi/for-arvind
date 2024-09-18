from confluent_kafka import avro

update_current_job_schema = avro.loads("""
    {
      "doc": "member update current jobs schema value",
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
          "doc": "Member company_address",
          "name": "company_address",
          "type": "string"
        },
        {
          "doc": "Member company_address_prov",
          "name": "company_address_prov",
          "type": "string"
        },
        {
          "doc": "Member company_address_dist",
          "name": "company_address_dist",
          "type": "string"
        },
        {
          "doc": "Member company_address_sub_dist",
          "name": "company_address_sub_dist",
          "type": "string"
        },
        {
          "doc": "Member company_address_postal_code",
          "name": "company_address_postal_code",
          "type": "string"
        },
        {
          "doc": "Member company_establish_from",
          "name": "company_establish_from",
          "type": "string"
        },
        {
          "doc": "Member company_unit_category",
          "name": "company_unit_category",
          "type": "string"
        },
        {
          "doc": "Member jobs_started_date",
          "name": "jobs_started_date",
          "type": "string"
        },
        {
          "doc": "Member jobs_status",
          "name": "jobs_status",
          "type": "string"
        },
        {
          "doc": "Member jobs_salary",
          "name": "jobs_salary",
          "type": "float"
        },
        {
          "doc": "Member jobs_placement",
          "name": "jobs_placement",
          "type": "string"
        },
        {
          "doc": "Member jobs_evident",
          "name": "jobs_evident",
          "type": "string"
        }
      ],
      "name": "memberUpdateJobsLoan",
      "namespace": "com.koperasi.member",
      "type": "record"
    }
""")