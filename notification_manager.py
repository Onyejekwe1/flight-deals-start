import os
import requests
from twilio.rest import Client

TWILIO_ACCT_ID = os.environ["TWILIO_ACCT_ID"]
TWILIO_AUTH_ID = os.environ["TWILIO_AUTH_ID"]

class NotificationManager:
    def __init__(self):
        pass

    def send_msg(self, msg: str, phone_no: str):
        client = Client(TWILIO_ACCT_ID, TWILIO_AUTH_ID)
        message = client.messages \
            .create(
                body=msg,
                from_='+15015107946',
                to=phone_no
            )