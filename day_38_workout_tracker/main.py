import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

nutritionix_api_key = os.environ.get("NUTRITIONIX_API_KEY")
nutritionix_app_id = os.environ.get("NUTRITIONIX_APP_ID")
sheety_auth_token = os.environ.get("SHEETY_AUTH_TOKEN")
google_sheet_id = os.environ.get("GOOGLE_SHEET_ID")

nutritionix_base_url = "https://trackapi.nutritionix.com"
sheety_base_url = f"https://api.sheety.co/{google_sheet_id}/myWorkouts/workouts"

date = datetime.now()

requests_header = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
    "Content-Type": "application/json"

}

request_body = {
    "query": input("Tell me what exercises you did: ")
}

response = requests.post(url=f"{nutritionix_base_url}/v2/natural/exercise", headers=requests_header, json=request_body).json()

list_of_workouts = response["exercises"]
get_workout_data = list_of_workouts[0]

sheety_requests_header = {
    "Authorization": f"Bearer {sheety_auth_token}"
}

for workout in range(len(list_of_workouts)):
    get_workout_data = list_of_workouts[workout]

    google_sheet_body = {
        "workout": {
            "date": date.strftime("%Y/%m/%d"),
            "time": date.strftime("%I:%M:%S %p"),
            "exercise": get_workout_data["name"].title(),
            "duration": get_workout_data["duration_min"],
            "calories": get_workout_data["nf_calories"],
        }
    }

    post_workout_on_google = requests.post(url=sheety_base_url, headers=sheety_requests_header, json=google_sheet_body)


