import requests as req
from datetime import datetime as dt
USERNAME = "dickielierman"
TOKEN = "985ljrtngd9f8y345n"
GRAPH_ID = 'graph1'
date = dt.now().strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Hours Worked",
    "unit": "hour",
    "type": "int",
    "color": "momiji"
}

graph_update_params = {
    "id": GRAPH_ID,
    "name": "Hours Worked",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

graph_entry_params = {
    "date": str(date),
    "quantity": "2",
}

graph_update_entry_params = {
    "quantity": "7",
}

# Create user
# resp = req.post(pixela_endpoint, json=user_params)

# Create Graph
# resp = req.post(graphs_endpoint, headers=headers, json=graph_params)

# Update Graph
# resp = req.put(f"{graphs_endpoint}/{GRAPH_ID}", headers=headers, json=graph_update_params)

# Create entry
# resp = req.post(f"{graphs_endpoint}/{GRAPH_ID}", headers=headers, json=graph_entry_params)

# Update entry
# resp = req.put(f"{graphs_endpoint}/{GRAPH_ID}/{date}", headers=headers, json=graph_update_entry_params)

# delete entry
# resp = req.delete(f"{graphs_endpoint}/{GRAPH_ID}/{date}", headers=headers)
print(resp.text)