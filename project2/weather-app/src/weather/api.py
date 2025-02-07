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