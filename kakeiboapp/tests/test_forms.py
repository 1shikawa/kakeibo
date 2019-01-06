from django.test import TestCase
from kakeiboapp.models import Category, Kakeibo
from kakeiboapp.forms import KakeiboForm
from datetime import datetime


# Create your tests here.
class KakeiboFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('kakeiboapp/test_forms_KakeiboFormTest is startred.')
        Category.objects.create(category_name='カテゴリ1')

    # def test_form(self):
    #     form_data = {'money': 1000,
    #                  'category_1': 1,
    #                     }
    #     form = KakeiboForm(data=form_data)
    #     self.assertTrue(form.is_valid())
