# ...existing code...
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Movie

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        for i in range(15):
            Movie.objects.create(
                title=f'Movie{i}',
                genre='Action' if i % 2 == 0 else 'Drama',
                release_date=f'2020-01-{i+1:02d}',
                rating=5.0 - (i * 0.1)
            )

    def test_filter_genre(self):
        response = self.client.get('/api/movies/?genre=Action')
        self.assertEqual(response.status_code, 200)
        for movie in response.data['results']:
            self.assertEqual(movie['genre'], 'Action')

    def test_filter_release_date_range(self):
        response = self.client.get('/api/movies/?release_date_after=2020-01-05&release_date_before=2020-01-10')
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        response = self.client.get('/api/movies/?limit=5&offset=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 5)

    def test_ordering(self):
        response = self.client.get('/api/movies/?ordering=release_date,rating')
        self.assertEqual(response.status_code, 200)
