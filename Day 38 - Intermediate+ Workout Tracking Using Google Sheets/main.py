from os import environ as env
import requests
from datetime import datetime as dt

GENDER = "male"
WEIGHT_KG = 90.7185
HEIGHT_CM = 182.88
AGE = 42
NUTRITIONIX_API_ID = env.get('NUTRITIONIX_API_ID')
NUTRITIONIX_API_KEY = env.get('NUTRITIONIX_API_KEY')

sheety_api = f'https://api.sheety.co/{env.get("SHEETY_USER")}/workoutTracking/workouts'
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


def parce_exercises(exercise_text):
    headers = {
        "x-app-id": NUTRITIONIX_API_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
    }
    parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(exercise_endpoint, json=parameters, headers=headers)
    result = response.json()['exercises']
    for data in result:
        d = {
            "workout": {
                "date": dt.now().strftime('%d/%m/%Y'),
                "time": dt.now().strftime('%M:%S:%f')[:8],
                "exercise": data['name'].title(),
                "duration": str(data['duration_min']),
                "calories": data['nf_calories']
            }
        }
        h = {
            "Content-Type":"application/json",
            "Authorization": env.get("SHEETY_BEARER")
        }
        resp = requests.post(sheety_api, headers=h,  json=d)
        print(resp.text)


entering_data = True
while entering_data:
    exercise_text = input("Tell me which exercises you did: ")
    if exercise_text in ['q', 'quit', 'end']:
        entering_data = False
        break
    else:
        parce_exercises(exercise_text)
