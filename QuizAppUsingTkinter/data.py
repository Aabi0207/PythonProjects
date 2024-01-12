import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
response_data = response.json()

question_data = response_data["results"]