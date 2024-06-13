from bs4 import BeautifulSoup
import requests
import smtplib

TARGET_PRICE = 150

AMAZON_LG_ITEM_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
SENDER_EMAIL = ""
RECEIVER_EMAIL = ""
APP_PASS = ""

REQUEST_HEADER = {
    "Accept-Language": "es-US,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
amazon_response = requests.get(url=AMAZON_LG_ITEM_URL, headers=REQUEST_HEADER).text
soup = BeautifulSoup(amazon_response, "html.parser")

amazon_lg_price_selector = soup.select_one("span .a-price-whole")

amazon_lg_price = int(amazon_lg_price_selector.getText().replace(".", ""))


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=APP_PASS)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=SENDER_EMAIL,
            msg=f"Subject: AMAZON PRICE ALERT! \n\n The price for the Electric Pressure Cooker: {AMAZON_LG_ITEM_URL}"
        )


if amazon_lg_price < TARGET_PRICE:
    send_email()
