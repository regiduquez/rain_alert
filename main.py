import requests as rq

API_KEY = "8277697bc90ebea4d8369b0622b1491f"
WEATHER_ENDP = "https://api.openweathermap.org/data/2.5/forecast"
PARAMS = {
    "lat": "35.604",
    "lon": "-134.429",
    "appid": API_KEY,
    "cnt": 4
}


response = rq.get(url=WEATHER_ENDP,params=PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]
for i in weather_list:
    if i['weather'][0]["id"] < 700:
        print("Bring Your Umbrella")
        weather = i['weather'][0]["main"]
        date, time = i["dt_txt"].split(" ")

        print(f"It will {weather} today at {time}")
        break
    else:
        continue

