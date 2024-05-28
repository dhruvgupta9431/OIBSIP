import requests

api_key = '057cb0855e2cccb44eca5210d7b524a7'
city_name = input("Enter Your Location:")
weather_data = (requests.get
                (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}"))

if weather_data.json()['cod'] == '404':

    print("No City Found!!!Try again")

else:
 weather = weather_data.json()['weather'][0]['main']

 temp = round(weather_data.json()['main']['temp'])

 humidity = weather_data.json()['main']['humidity']

 temp_max = weather_data.json()['main']['temp_max']

 temp_min = weather_data.json()['main']['temp_min']

print(f"Weather  : {weather}")

print(f"Temperature : {temp}ºC")

print(f"Humidity  : {humidity}")

print(f"Temp_max  : {temp_max}ºC")

print(f"Temp_min : {temp_min}ºC")

print(f"...........................")

print(f"....Thank You For Using....")
