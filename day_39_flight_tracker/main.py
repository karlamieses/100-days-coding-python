from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()

flight_search = FlightSearch()
flight_search.search_flights_using_iata_codes()
