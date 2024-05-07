from dotenv import load_dotenv
from flight_search import FlightSearch
from data_manager import DataManager

load_dotenv()


print("Welcome to Karla's Flight Club")
print("We find the best flight deals and email you")

data_manager = DataManager()
data_manager.introduce_user()

flight_search = FlightSearch()
flight_search.search_flights_using_iata_codes()

