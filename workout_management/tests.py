from django.test import TestCase
from django.contrib.auth.models import User
from workout_management.models import Activity
from datetime import date

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_activity(self):
        activity = Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration=45,
            distance=10.0,
            calories_burned=500,
            date=date.today()
        )
        self.assertEqual(str(activity), f"{self.user.username} - Running on {date.today()}")
        self.assertEqual(activity.duration, 45)
