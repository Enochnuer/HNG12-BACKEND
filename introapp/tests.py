from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

class InfoViewTest(TestCase):
    def test_get_info(self):
        url = reverse('display_info')  # Use the correct URL name
        response = self.client.get(url, HTTP_ACCEPT='application/json')  # Set the Accept header to JSON
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(str(response.content, 'utf-8'), {
            "email": "enochnuer111@gmail.com",
            "current_datetime": "2025-01-30T12:19:2Z",  # Update with the actual expected datetime
            "github_url": "https://github.com/Enochnuer/HNG12-BACKEND"
        })