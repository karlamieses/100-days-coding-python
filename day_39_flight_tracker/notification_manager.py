import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCT_ID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


class NotificationManager:
    def __init__(self, price, city, from_flight_date, to_flight_date, airport_code, sheety_price):
        self.client = Client(account_sid, auth_token)
        self.message = self.client.messages.create(
            body=f"Low price alert! Only USD${price} to flight from London-Heathrow, to {city}-{airport_code}, from {from_flight_date} to {to_flight_date}, before was USD${sheety_price}",
            from_="+12132237454",
            to="+447393036904"
        )
