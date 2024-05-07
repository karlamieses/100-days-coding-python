import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to Google Sheet
    def __init__(self):
        self.get_lowest_prices = None
        self.get_lowest_price = None
        self.only_iata_code_list = None
        self.sheety_records_list = None
        self.sheety_response = None
        self.google_sheet_id = os.environ.get("GOOGLE_SHEET_ID_FLIGHT_TRACKER")
        self.sheety_endpoint = f"https://api.sheety.co/{self.google_sheet_id}/flightDeals"
        self.sheety_header = {
            "Authorization": f"Bearer {os.environ.get("SHEETY_AUTH_TOKEN_FLIGHT_FINDER")}"
        }

    def read_google_sheet(self):
        self.sheety_response = requests.get(url=f"{self.sheety_endpoint}/prices", headers=self.sheety_header).json()
        return self.sheety_response

    def get_iata_codes(self):
        # Get iataCode from sheety to use it when sending the request to search for flights.
        self.sheety_records_list = self.read_google_sheet()
        self.only_iata_code_list = []

        for index in range(len(self.sheety_records_list["prices"])):
            self.only_iata_code_list.append(self.sheety_records_list["prices"][index]["iataCode"])

        return self.only_iata_code_list

    def introduce_user(self):
        #Introduce user list into Google Sheet -> User tab
        sheety_params = {
            "user": {
                "firstName": input("What is your name? \n"),
                "lastName": input("What is your last name?\n"),
                "email": input("What is your email?\n")
            }
        }

        print("You are in the club")

        url = f"{self.sheety_endpoint}/users"

        sheety_response = requests.post(url=url, headers=self.sheety_header, json=sheety_params)

    def alert_all_sheety_user(self):
        # Get all the user list member to send an email
        url = f"{self.sheety_endpoint}/users"
        sheety_response = requests.get(url=url, headers=self.sheety_header).json()

        get_emails = sheety_response["users"]

        email_list = []

        for user in get_emails:
            email = user["email"]

            email_list.append(email)

        return email_list

