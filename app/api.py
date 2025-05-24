# app/api.py
import requests

def get_coordinates(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "format": "json"}
    response = requests.get(geo_url, params=params)
    data = response.json()
    
    if "results" not in data or not data["results"]:
        raise ValueError("City not found.")
    
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather_data(city):
    lat, lon, city_name = get_coordinates(city)
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(weather_url, params=params)
    data = response.json()

    return {
        "city": city_name,
        "temperature": data["current_weather"]["temperature"]
    }
