from django.conf import settings
import requests

def send_simple_message(to, subject, text, sender=None):
    return requests.post(
        settings.EMAIL_MAILGUN_URL,
        auth=("api", settings.EMAIL_MAILGUN_API_KEY),
        data={"from": sender or settings.EMAIL_MAILGUN_DEFAULT_SENDER,
              "to": to,
              "subject": subject,
              "text": text})
    