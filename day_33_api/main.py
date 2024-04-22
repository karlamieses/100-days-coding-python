import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_closed():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS COORDINATES ARE: ({iss_latitude, iss_longitude})")

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LAT + 5 >= iss_longitude >= MY_LAT - 5:
        print(iss_latitude)
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
my_time = time_now.hour

sender_email = ""
sender_password = "t"
receiver_email = ""
message = "Subject: LOOK UP! ISS IS ON TOP \n\n LOOK UP!"


def notify_me(sender, sender_pass, receiver, mail_content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(sender, sender_pass)
        connection.sendmail(from_addr=sender, to_addrs=receiver, msg=mail_content)


if my_time <= sunrise or my_time >= sunset:
    while is_iss_closed():
        notify_me(sender=sender_email, sender_pass=sender_password, receiver=receiver_email, mail_content=message)
        time.sleep(60)
