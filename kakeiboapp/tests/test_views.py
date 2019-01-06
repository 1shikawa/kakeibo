from django.test import TestCase
from kakeiboapp.models import Category, Kakeibo

# Create your tests here.
class KakeiboTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('kakeiboapp/test_views_KakeiboTest is starterd.')

    @classmethod
    def tearDownClass(cls):
        print('kakeiboapp/test_views_KakeiboTest is end.')

    def test_get_kakeibo_nodata(self):
        kakeibo_data = Kakeibo.objects.all().count()
        self.assertEqual(kakeibo_data, 1)

    def test_get_kakeibo_list(self):
        response = self.client.get('/kakeiboapp/kakeibo_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kakeiboapp/kakeibo_list.html')

    def test_get_kakeibo_create(self):
        response = self.client.get('/kakeiboapp/kakeibo_create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kakeiboapp/kakeibo_form.html')

    def test_get_kakeibo_update(self):
        response = self.client.get('/kakeiboapp/kakeibo_update/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kakeiboapp/kakeibo_form.html')

    def test_get_kakeibo_delete(self):
        response = self.client.get('/kakeiboapp/kakeibo_delete/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kakeiboapp/kakeibo_confirm_delete.html')

    def test_get_kakeibo_circle(self):
        response = self.client.get('/kakeiboapp/circle/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kakeiboapp/kakeibo_circle.html')
