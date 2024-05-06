import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv()

LONDON_HEATHROW_IATA_CODE = "LHR"


class FlightSearch(DataManager, NotificationManager):
    # This class is responsible for talking to tequila (Flight Search API)
    def __init__(self):
        super().__init__()
        self.get_airport_info = None
        self.date = datetime.now() + timedelta(30)
        self.from_date_flight = self.date.strftime("%Y-%m-%d")
        self.return_date_flight = (self.date + timedelta(15)).strftime("%Y-%m-%d")
        self.params = None
        self.serpapi_endpoint = "https://serpapi.com/search.json"

    def search_flights_using_iata_codes(self):
        # Make a request per IATA CODE

        iata_list = self.get_iata_codes()

        print(iata_list)

        for code in iata_list:
            self.params = {
                "engine": "google_flights",
                "departure_id": f"{LONDON_HEATHROW_IATA_CODE}",
                "arrival_id": f"{code}",
                "outbound_date": f"{self.from_date_flight}",
                "return_date": f"{self.return_date_flight}",
                "currency": "USD",
                "hl": "en",
                "stops": "1",
                "api_key": os.environ.get("SERPAPI_API_KEY"),
            }

            get_flights_info_response = requests.get(url=self.serpapi_endpoint, params=self.params).json()
            get_flight_price = [get_flights_info_response["best_flights"][index]["price"] for index in
                                range(len(get_flights_info_response["best_flights"]))]
            print(get_flight_price)
            self.get_airport_info = get_flights_info_response["search_parameters"]["arrival_id"]

            self.compare_price_with_google_sheet(new_flight_price=min(get_flight_price), iata_code=code)

    def compare_price_with_google_sheet(self, new_flight_price, iata_code):
        # this take the price from the search response json, and compare it with the flight in Google Sheet

        current_flight_prices = self.read_google_sheet()

        for price_info in current_flight_prices["prices"]:
            if price_info["iataCode"] == iata_code:
                get_iata_city = price_info["city"]
                get_iata_code_price = price_info["lowestPrice"]
                if int(new_flight_price) < int(get_iata_code_price):
                    # here we need to send SMS
                    notification_manager = NotificationManager(price=new_flight_price, city=get_iata_city, airport_code=self.get_airport_info,  from_flight_date=self.from_date_flight, to_flight_date=self.return_date_flight, sheety_price=get_iata_code_price)

