import requests
import pandas as pd
from .models import WeatherData
from datetime import datetime

API_TOKEN = "AwQPoSWAnhfoBWIZVUEnDSxLQNqtdHpy" # replace
BASE_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
headers = {"token": API_TOKEN}

params = {
    "datasetid": "GHCND",  
    "locationid": "FIPS:AR",#control
    "startdate": "2024-03-01",
    "enddate": "2024-03-10",
    "limit": 1000
}

def fetch_noaa_data():
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get("results", ["kkjk"])
        for entry in data:
            WeatherData.objects.update_or_create(
                city="Buenos Aires",
                date=datetime.fromisoformat(entry["date"]),
                defaults={
                    "temperature": entry.get("value", 0),
                    "humidity": entry.get("humidity", 0),
                    "wind_speed": entry.get("windSpeed", 0),
                }
            )
        return True
    return False
