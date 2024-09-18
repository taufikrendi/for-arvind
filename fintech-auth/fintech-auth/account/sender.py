import threading


def email_threading(email):
    email.send(fail_silently=False)
    threading.Thread.__init__(email)