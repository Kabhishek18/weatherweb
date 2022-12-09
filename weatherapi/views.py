import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import City
from .form import CityFormRequest

def kevingToCelcius(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) +32
    return celcius, fahrenheit


def index(request):
    # Form 
    if request.method == 'POST':
        form = CityFormRequest(request.POST)
        form.save()

    form = CityFormRequest()

    api_url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key ='5549e7f74a744927a21e9a00796c8b29'
    #metric ='&units=metric'
   
    
    cities = City.objects.all()

    weather_data = []
    countid = 0
    for city in cities:
        url = api_url +"appid=" +api_key +"&q=" + city.name 
        r = requests.get(url).json()
            
        temp_in_kelvin = r['main']['temp']
        celcius, fahrenheit =kevingToCelcius(temp_in_kelvin)
        countid = countid + 1 
        city_weather = {
            'id' : countid,
            'city': city.name,
            'temperature_C': celcius,
            'temperature_f': fahrenheit,
            'temperature_k': temp_in_kelvin,
            'humdity': r['main']['humidity'],
            'weather': r['weather'][0]['main'],
            'visibility': r['visibility'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = { 'title':'☔️ Weather App','weather_data': weather_data, 'form': form}

    return render(request,'index.html',context)

