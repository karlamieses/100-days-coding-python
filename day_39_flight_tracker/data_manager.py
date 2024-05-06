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
        self.sheety_endpoint = f"https://api.sheety.co/{self.google_sheet_id}/flightDeals/prices"

    def read_google_sheet(self):
        self.sheety_response = requests.get(url=self.sheety_endpoint).json()
        return self.sheety_response

    def get_iata_codes(self):
        # Get iataCode from sheety to use it when sending the request to search for flights.
        self.sheety_records_list = self.read_google_sheet()
        self.only_iata_code_list = []

        for index in range(len(self.sheety_records_list["prices"])):
            self.only_iata_code_list.append(self.sheety_records_list["prices"][index]["iataCode"])

        return self.only_iata_code_list
