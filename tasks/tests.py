from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Task 

class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {
            'title': 'Test Task',
            'status': 'todo'
        }

        response = self.client.post('/api/tasks/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


    def test_get_single_task(self): 
        task = Task.objects.create(title='Test Task', status='todo', owner=self.user)

        response = self.client.get(f'/api/tasks/{task.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')


    def test_patch_task(self):

        task = Task.objects.create(title='Test Task', status='todo', owner=self.user)

        response = self.client.patch(
            f'/api/tasks/{task.id}/',
            {'status': 'done'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, 'done')

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', status='todo', owner=self.user)

        response = self.client.delete(f'/api/tasks/{task.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    
    def test_unauthenticated_access(self):
        self.client.credentials()
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cannot_see_other_users_tasks(self): 
        other_user = User.objects.create_user(
            username = 'otheruser',
            password = 'otherpass123'
        )
        Task.objects.create(title = 'Fremder Task', status = 'todo', owner = other_user)

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)


    def test_invalid_status_rejected(self): 
        data = {
            'title': 'Test Task', 
            'status': 'ungültig'
        }
        response = self.client.post('/api/tasks/', data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)