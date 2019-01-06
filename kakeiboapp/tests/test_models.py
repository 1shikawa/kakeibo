from django.test import TestCase
from kakeiboapp.models import Kakeibo, Category
from datetime import datetime

# Create your tests here.
class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('kakeiboapp/test_models_CategoryTest is startred.')
        Category.objects.create(category_name='カテゴリ1')

    @classmethod
    def tearDownClass(cls):
        print('kakeiboapp/test_models_CategoryTest is end.')

    def test_Category_label(self):
        category1 = Category.objects.get(id=1)
        category1_label = category1._meta.get_field('category_name').verbose_name
        self.assertEqual(category1_label, 'カテゴリ')

    def test_Category_data(self):
        category1 = Category.objects.get(id=1)
        category1_data = category1.category_name
        self.assertEqual(category1_data, 'カテゴリ1')


class KakeiboTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('kakeiboapp/test_models_KakeiboTest is startred.')
        Category.objects.create(category_name='食費')
        Kakeibo.objects.create(memo='外食', money=1000, category_id=1)

    @classmethod
    def tearDownClass(cls):
        print('kakeiboapp/test_models_KakeiboTest is end.')

    def test_Kakeibo_label(self):
        kakeibo1 = Kakeibo.objects.get(id=1)
        kakeibo1_label = kakeibo1._meta.get_field('money').verbose_name
        self.assertEqual(kakeibo1_label, '金額')

    def test_Kakeibo_data_money(self):
        kakeibo1 = Kakeibo.objects.get(id=1)
        kakeibo1_data = kakeibo1.money
        self.assertEqual(kakeibo1_data, 1000)

    def test_Kakeibo_data_memo(self):
        kakeibo1 = Kakeibo.objects.get(id=1)
        kakeibo1_data = kakeibo1.memo
        self.assertEqual(kakeibo1_data, '外食')

    def test_Kakeibo_data_category(self):
        kakeibo1 = Kakeibo.objects.get(id=1)
        kakeibo1_data = kakeibo1.category_id
        self.assertEqual(kakeibo1_data, 1)

    # def test_Kakeibo_data_date(self):
    #     kakeibo1 = Kakeibo.objects.get(id=1)
    #     kakeibo1_data = kakeibo1.date
    #     self.assertEqual(kakeibo1_data, '2019-01-07')
