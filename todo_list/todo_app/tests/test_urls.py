from django.test import SimpleTestCase
from django.urls import reverse,resolve
from todo_app.views import home,delete,update,todo_listAPI
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)
    # def test_list_url_update(self):
    #     url = reverse('update_list',args=[31])
    #     print(resolve(url))
    
