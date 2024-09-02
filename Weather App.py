import requests

def fetch_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None

def display_weather(data):
    if data:
        city_name = data.get('name')
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather data.")

def main():
    api_key = "b5c7c518203606445ff1d07ddb7244c0"
    
    city = input("Enter the city name: ")
    
    weather_data = fetch_weather(city, api_key)
    
    display_weather(weather_data)

if __name__ == "__main__":
    main()
