from django.test import TestCase
from kakeiboapp.models import Category, Kakeibo
from kakeiboapp.forms import KakeiboForm
from datetime import datetime


# Create your tests here.
class KakeiboFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('kakeiboapp/test_forms_KakeiboFormTest is startred.')

    def test_form_is_valid(self):
        category = Category.objects.create(category_name='食費')
        form_data = {
            'money': 1000,
            'category': category.pk,
            'memo': '外食',
            'date': datetime.now()
        }
        form = KakeiboForm(data=form_data, instance=category)
        self.assertTrue(form.is_valid())

    def test_form_is_unvalid(self):
        category = Category.objects.create(category_name='カテゴリ1')
        form_data = {
            'money': '二千円',
            'date': datetime.now(),
            'memo': '出張',
            'category': category.pk # categoryではない
        }
        form = KakeiboForm(form_data, instance=category)
        self.assertFalse(form.is_valid())
