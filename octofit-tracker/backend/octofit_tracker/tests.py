from django.test import TestCase
from .models import Team, CustomUser, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team, team)

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5)
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        workout = Workout.objects.create(user=user, name='Leg Day', description='Squats')
        self.assertEqual(workout.name, 'Leg Day')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)
