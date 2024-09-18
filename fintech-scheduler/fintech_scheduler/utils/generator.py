import uuid, hashlib, base64
from random import randint

def generator_uuid():
    generate = hashlib.sha1(base64.urlsafe_b64encode(uuid.uuid4().bytes)).hexdigest()
    return generate


def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)