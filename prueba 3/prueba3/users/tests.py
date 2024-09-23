from django.test import TestCase
from rest_framework.test import APIClient

class PostUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_user(self):
        response = self.client.post('/api/post_user/', {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'preferences': '1,3,7',
            'affiliate': 'true'
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'User created successfully')
