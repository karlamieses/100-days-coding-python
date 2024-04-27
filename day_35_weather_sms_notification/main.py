import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

weather_auth_token = os.environ.get("WEATHER_AUTH_TOKEN")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_acct_id = os.environ.get("TWILIO_ACCT_ID")
twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")

weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": "51.590315762049784",
    "lon": "-0.01716631269677842",
    "appid": weather_auth_token,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_report = response.json()["list"]

will_rain = False
for forecast in weather_report:
    get_weather_code = forecast["weather"][0]["id"]
    get_time_of_rain = forecast["dt_txt"].split()[1].split(":")[0]

    if get_weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_acct_id, twilio_auth_token)
    message = client.messages.create(body="Remember to bring the umbrella ☔️",
                                     from_="+12132237454", to="+447393036904")
