from django.shortcuts import render
from dotenv import load_dotenv
import requests, json, os

load_dotenv()

nasa_url = os.getenv("nasa_url")

def get_data():
    response = requests.get(nasa_url)
    data = response.json()
    print(data)
    return(data)

def index(request):
    context = {
        'data' : get_data(),
    }
    return render(request, "index.html", context)
