import requests

def weather(city):
    res = requests.get("http://api.weatherbit.io/v2.0/current?city="+city+"&key=a91d911ef70844758f29735346af06e4&include=minutely")
    if res.status_code == 200:
        val= res.json()
        weather_data={
            'temp':val['data'][0]['temp'],
            'clouds':val['data'][0]['clouds'],
            'windspd':val['data'][0]['wind_spd'],
            'name':val['data'][0]['city_name']
        }
    
    else:
        print("nope")
    return weather_data

