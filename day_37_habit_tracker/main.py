import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPH_ID = "coding-journey"

create_user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create users
response = requests.post(url=pixela_endpoint, json=create_user_body)

create_graph_header = {
    "X-USER-TOKEN": "randomToken@123"
}

create_graph_body = {
    "id": "coding-journey",
    "name": "coding",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

# Create graph
create_graph = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", json=create_graph_body, headers=create_graph_header)

get_graph_endpoint = requests.get(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}") # Graph: https://pixe.la/v1/users/pythonwithkarla/graphs/coding-journey.html


# Post values on the graph
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

post_graph_body = {
    "date": f"{formatted_date}",
    "quantity": "10"
}

# yyyyMMdd

# post_in_graph = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=post_graph_body,
#                               headers=create_graph_header)


put_graph_body = {
    "quantity": "3"
}

update_graph = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240410", headers=create_graph_header, json=put_graph_body, )


delete_pixel = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240410", headers=create_graph_header, json=put_graph_body)


delete_graph = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}")