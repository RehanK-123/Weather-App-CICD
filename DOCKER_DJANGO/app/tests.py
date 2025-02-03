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

class URLTest(TestCase):
    def test_url_home(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, views.home)

    def test_url_weather(self):
        url = reverse("weather")
        self.assertEqual(resolve(url).func, views.weather)
    
# Create your tests here.
