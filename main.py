import os
import requests as rq
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


ACC_SID = os.environ.get('ACCOUNT_SID')
AUTH_KEY = os.environ.get('AUTHENTICATION_KEY')
MY_MOBILE = os.environ.get('MY_MOB_NO')

API_KEY = "8277697bc90ebea4d8369b0622b1491f"
WEATHER_ENDP = "https://api.openweathermap.org/data/2.5/forecast"
PARAMS = {
    "lat": "14.691770",
    "lon": "120.538582",
    # "lat": "33.804",
    # "lon": "-118.251",
    "appid": API_KEY,
    "cnt": 4
}


response = rq.get(url=WEATHER_ENDP,params=PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]
will_rain = False
for i in weather_list:
    if i['weather'][0]["id"] < 700:
        print("Bring Your Umbrella")
        weather = i['weather'][0]["main"]
        date, time = i["dt_txt"].split(" ")

        print(f"It will {weather} today at {time}")
        will_rain = True
        break
    else:
        continue

if will_rain:
    # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(ACC_SID, AUTH_KEY ) #http_client=proxy_client
    message = client.messages \
    .create(
        body= "It's going to rain today, don't forget to bring an ☂️ ",
        from_= "+18285481059",
        to= MY_MOBILE,
    )
    print(message.status)
