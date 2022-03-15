from django.shortcuts import render
from dotenv import load_dotenv
import requests, json, os

load_dotenv()

nasa_url = os.getenv("nasa_url")
rover_photo = os.getenv("rover_photo")
mars_weather = os.getenv("mars_weather")

def get_data():
    response = requests.get(nasa_url)
    data = response.json()
    print(data)
    return(data)

def get_photo():
    response = requests.get(rover_photo)
    photo = response.json()
    print(photo)
    return(photo)

def get_mars_weather():
    response = requests.get(mars_weather)
    weather = response.json()
    print(weather)
    return(weather)


def index(request):
    context = {
        'data' : get_data(),
        'photo' : get_photo(),
        'weather' : get_mars_weather(),
    }
    return render(request, "index.html", context)

