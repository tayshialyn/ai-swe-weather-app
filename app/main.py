import requests

def get_coordinates(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "format": "json"
    }
    response = requests.get(geo_url, params=params)
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError("City not found.")
    
    result = data["results"][0]
    return result["latitude"], result["longitude"]

def get_current_temperature(lat, lon):
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(weather_url, params=params)
    data = response.json()
    
    return data["current_weather"]["temperature"]

def main():
    city = input("Enter city name: ")
    try:
        lat, lon = get_coordinates(city)
        temperature = get_current_temperature(lat, lon)
        print(f"The current temperature in {city} is {temperature}°C.")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    main()
