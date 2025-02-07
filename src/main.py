from weather.api import get_weather_data

def display_weather(city_name):
    weather_data = get_weather_data(city_name)
    
    if weather_data:
        current_condition = weather_data['current_condition'][0]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {current_condition['temp_C']}°C")
        print(f"Feels Like: {current_condition['FeelsLikeC']}°C")
        print(f"Weather Description: {current_condition['weatherDesc'][0]['value']}")
    else:
        print(f"Could not retrieve weather data for {city_name}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_weather(city_name)