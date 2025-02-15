from django.test import TestCase
from unittest.mock import Mock, patch
from django.urls import reverse, resolve
import requests
from . import views


class ViewTest(TestCase):
    def test_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)    
        self.assertTemplateUsed(response, 'Weather_app.html') 
    
    @patch("app.views.requests.get")
    def test_weather_page(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data" : {"values" : {"cloudCover" : 1,"humidity" : 2, "temperature" : 3, "precipitationProbability" : 4, "windSpeed" : 5, "temperatureApparent" : 6}}}
        mock_get.return_value = mock_response

        response = self.client.post(reverse("weather"), {"city" : "Pune"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'App.html')

class URLTest(TestCase):
    def test_url_home(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, views.home)

    def test_url_weather(self):
        url = reverse("weather")
        self.assertEqual(resolve(url).func, views.weather)
    
# Create your tests here.
