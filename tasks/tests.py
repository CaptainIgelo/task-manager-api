from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task 

class TaskAPITests(APITestCase):

    def test_get_all_tasks(self):
        # Act
        response = self.client.get('/api/tasks/')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        # Arrange 
        data = {
            'title': 'Test Task',
            'status': 'todo'
        }

        # Act
        response = self.client.post('/api/tasks/', data, format='json')

        # Assert 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


    def test_get_single_task(self): 
        # Arrange 
        task = Task.objects.create(title='Test Task', status='todo')

        # Act 
        response = self.client.get(f'/api/tasks/{task.id}/')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')


    def test_patch_task(self):

        #Arrange
        task = Task.objects.create(title='Test Task', status='todo')

        # Act
        response = self.client.patch(
            f'/api/tasks/{task.id}/',
            {'status': 'done'},
            format='json'
        )

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, 'done')

    def test_delete_task(self):
        # Arrange
        task = Task.objects.create(title='Test Task', status='todo')

        # Act
        response = self.client.delete(f'/api/tasks/{task.id}/')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)