import threading


def email_threading(self, email):
    self.email = email
    self.email.send(fail_silently=False)
    threading.Thread.__init__(self)

# class EmailThreading(threading.Thread):
#
#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)
#
#     def run(self):
#         self.email.send(fail_silently=False)