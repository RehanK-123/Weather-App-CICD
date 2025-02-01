from django.shortcuts import render
import requests

# Create your views here
def home(request):
    return render(request, 'Weather_app.html')

def weather(request):
    key = "dzTGZbGX7WlEb2qYexSwqAUfV3tvT7AO"
    if request.method == 'POST':
       city = request.POST.get('city')
    response = requests.get(url= f'https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={key}')
    data = response.json()
    dic = {}
    features = ["cloudCover","humidity", "temperature", "precipitationProbability", "windSpeed", "temperatureApparent"]
    # print(data)
    for i in features:
        dic[i] = data["data"]["values"][i]
        print(dic[i])
    return render(request, 'App.html', dic)