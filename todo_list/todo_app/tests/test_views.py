from django.test import TestCase,Client
from django.urls import reverse
from todo_app.models import todo_list
import json

class TestViews(TestCase):
    def setUp(self):
        self.client= Client()
        self.home_url=reverse('home')
        self.delete_url=reverse('delete_list',args=['31'])
        self.update_url=reverse('update_list',args=['31'])

    def test_project_list_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

    # def test_project_Delete_GET(self):
    #     print(self.delete_url)
    #     response = self.client.get(self.delete_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response,'home.html')
    #
    # def test_project_update_GET(self):
    #     print(self.update_url)
    #     response = self.client.get(self.update_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response,'home.html')

    def test_project_add_task(self):
        newTask=todo_list.objects.create(
            Title="My Testing Jobs",
            Description="My Test",
            DateTime_of_todo_task= datetime(2019-05-02 00:00:00),
            Status= "progress",
        )
        newTask.save()
