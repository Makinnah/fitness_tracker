from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from workout_management.models import Activity
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

class ActivityViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_activity(self):
        data = {
            "activity_type": "Cycling",
            "duration": 60,
            "distance": 20.0,
            "calories_burned": 600,
            "date": str(date.today())
        }
        response = self.client.post('/api/activities/', data)
        print("RESPONSE DATA:", response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Activity.objects.count(), 1)
