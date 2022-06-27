import requests
def weather_data(city_name,day):

    api_key="70fe7371be9749a78e990750222706"
    base_url = "http://api.weatherapi.com/v1/forecast.json?"
    complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&days=" + day
    response = requests.get(complete_url)
    x = response.json()
    print(x)

