from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
def send_the_mail():
    print "enter a recipient address"
    to = raw_input()
    print "enter a message"
    message = raw_input()
    send_mail(
        "DOJO CHIMP",
        message,
        EMAIL_HOST_USER,
        [to]
    )