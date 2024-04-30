import os
import datetime as dt
import requests

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

stock_market_api_key = os.environ.get("STOCK_MARKET_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
weather_auth_token = os.environ.get("WEATHER_AUTH_TOKEN")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_acct_id = os.environ.get("TWILIO_ACCT_ID")
twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")

stock_market_url = "https://www.alphavantage.co/query"
tesla_news = "https://newsapi.org/v2/everything"

datetime = dt.datetime.now()
date = datetime.date()
weekday = datetime.weekday()  # Saturday 5 and Sunday 6

stock_market_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "interval": "60min",
    "outputsize": "compact",
    "apikey": stock_market_api_key
}

news_params = {
    "q": "Tesla",
    "sortBy": "relevancy",
    "totalResults": 1,
    "apiKey": news_api_key
}


def send_sms(stock_info, title, news):
    client = Client(twilio_acct_id, twilio_auth_token)
    message = client.messages.create(body=f"{stock_info} \nHeadline️: {title}\n Brief: {news}",
                                     from_="+12132237454", to="+447393036904")


def get_news():
    response = requests.get(url=tesla_news, params=news_params).json()
    get_article = response["articles"][0]["title"]
    get_article_description = response["articles"][0]["description"]
    return get_article, get_article_description


def get_stock_market(today, yesterday):
    stock_market_response = requests.get(url=stock_market_url, params=stock_market_params).json()

    if today not in stock_market_response["Time Series (Daily)"]:
        headline = "No closing for TESLA yet"
        brief = "Tesla's Today's closing is not generated. This will be generated at 9pm today"
        send_sms(stock_info="✋🏼 Too Early For Closing", title=headline, news=brief)
    else:
        today_closing = float(stock_market_response["Time Series (Daily)"][today]["4. close"])
        yesterday_closing = float(stock_market_response["Time Series (Daily)"][yesterday]["4. close"])

        difference = round(today_closing - yesterday_closing, 4)
        difference_percentage = round(difference / 100, 4)

        if today_closing > yesterday_closing:
            headline, brief = get_news()
            send_sms(stock_info=f"TSLA 💹 {difference_percentage}.", title=headline, news=brief)
        else:
            headline, brief = get_news()
            send_sms(stock_info=f"TSLA 🔻{difference_percentage}.", title=headline, news=brief)


if weekday == 5:
    use_friday = date - dt.timedelta(1)
    day_before = use_friday - dt.timedelta(1)
    get_stock_market(today=str(use_friday), yesterday=str(day_before))
elif weekday == 6:
    use_friday = date - dt.timedelta(2)
    day_before = use_friday - dt.timedelta(1)
    get_stock_market(today=str(use_friday), yesterday=str(day_before))
elif weekday == 0:
    use_friday = date - dt.timedelta(3)
    date = "2024-04-24"
    get_stock_market(today=str(date), yesterday=str(use_friday))  ## Hardcoded for Demo
else:
    day_before = date - dt.timedelta(1)
    get_stock_market(today=date, yesterday=day_before)
