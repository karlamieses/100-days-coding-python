import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCT_ID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


class NotificationManager:
    def __init__(self, price, city, from_flight_date, to_flight_date, airport_code, sheety_price):
        self.message = (f"Low price alert! Only USD${price} to flight from London-Heathrow, to {city}-{airport_code}, "
                        f"from {from_flight_date} to {to_flight_date}, before was USD${sheety_price}")

    def send_sms(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=self.message,
            from_="+12132237454",
            to="+447393036904"
        )

    def send_email(self, receiver_email):
        sender_email = os.environ.get("SENDER_EMAIL")
        app_password = os.environ.get("SEND_EMAIL_PASSWORD")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(sender_email, app_password)
            connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                                msg=f"Subject: Low Alert! \n{self.message}")
