import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']

            print(f"Temperature in {city_name}: {temperature}°C")
            print(f"Humidity in {city_name}: {humidity}%")
            print(f"Sunrise in {city_name}: {format_time(sunrise)}")
            print(f"Sunset in {city_name}: {format_time(sunset)}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    import datetime
    
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the city name: ")
    get_weather(api_key, city_name)

