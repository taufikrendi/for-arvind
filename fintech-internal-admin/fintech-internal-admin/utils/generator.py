import uuid, hashlib, base64, logging, traceback

from cryptography.fernet import Fernet
from django.conf import settings
from random import randint


def generator_uuid():
    generate = hashlib.sha1(base64.urlsafe_b64encode(uuid.uuid4().bytes)).hexdigest()
    return generate


def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def encrypt(txt):
    try:
        txt = str(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(txt):
    try:
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

#url encrypt example using
#on master in many
# l = []
# For i in query:
# 	i['encrypt_key']=encrypt(i['id'])
# 	i['id']=i['i']
# 	l.append(i)

#on master in single

# i['encrypt_key']=encrypt(i['id'])

#on details
# pk_decrypt = decrypt(pk)
# in template tags xx.encrypt_key
# in url <str:id>