import requests

def get_weather_data(city_name):
    base_url = f"http://wttr.in/{city_name}"
    params = {
        'format': 'j1'  # JSON format
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_weather_data(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"Current weather in {city}: {temperature}°C, {description}."
    else:
        return "Weather data not available."