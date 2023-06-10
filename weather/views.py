from django.shortcuts import render
import requests 
from weather.models import City
from weather.forms import CityForm


def home(request):
    api_key = '6864579cc58468bc999a8d8aa8b874a1'
    api_url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key
    
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()   

    api_city = City.objects.all() #Берём все элементы из таблички City
    all_city = []
    # Берём все необходиммые данные из Api и саписываем в словарь.
    for city in api_city:
        res = requests.get(api_url.format(city.name)).json()
        city_info = {
            'сity': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        # Затем все данные записываем в список и вывводим его.
        all_city.append(city_info)
    context = {'all_info':  all_city, 'form': form}
    return render(request, 'weather/home.html',context)
