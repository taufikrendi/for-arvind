import logging
import unittest
from django.test import Client
from faker import Faker
fake = Faker()
logger = logging.getLogger(__name__)


class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def normal_post(self):
        url = 'http://127.0.0.1:5000/api/v1/account/profile/registrations/'

        data = {
            "email": fake.email(),
            "first_name": "first_name1",
            "password": "test password",
            "phone_number": fake.phone_number(),
            "agreement": "true"
        }
        response = self.client.post(url, data)
        if response.status_code != 200:
            logger.error('status code not 200')


    def huge_post(self):
        looping = 1000000
        url = 'http://127.0.0.1:5000/api/v1/account/profile/registrations/'

        for i in range(looping):
            data = {
                "email": fake.email(),
                "first_name": "first_name1",
                "password": "test password",
                "phone_number": fake.phone_number(),
                "agreement": "true"
            }
            response = self.client.post(url, data)



