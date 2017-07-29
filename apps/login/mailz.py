from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.conf.global_settings import EMAIL_HOST_USER, EMAIL_PORT
def send_the_mail(sender, pw, recipient, message):
    with get_connection(
        username=sender,
        password=pw
    ) as connection:
        print connection
        result = EmailMessage(
            "DOJO CHIMP",
            message,
            sender,
            [recipient],
            connection=connection
        ).send()
        print result
    # connection.close()

def send_the_mail_2(message, to):
    send_mail(
        "DOJO CHIMP",
        message,
        EMAIL_HOST_USER,
        [to]
    )