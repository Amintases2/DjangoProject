import requests
from django.test import TestCase


class TestForm(TestCase):

    def test_request1(self):
        # из 1ой формы
        data = {
            'question_text': 'test_text',
            'contact_phone': '+7 111 111 11 11',
        }
        response = requests.post("http://127.0.0.1:8000/form/get_form/", params=data)
        self.assertEqual(response.content, b'QuestionCreateForm')

    def test_request2(self):
        # из 2ой формы
        data = {
            'user_birthday': '11.11.2011',
            'user_email': 'test@mail.ru',
            'user_name': 'TestName',
        }
        response = requests.post("http://127.0.0.1:8000/form/get_form/", params=data)
        self.assertEqual(response.content, b'UserInfoForm')

    def test_request3(self):
        # из разных форм
        data = {
            'question_text': 'test_text',
            'contact_phone': '+7 111 111 11 11',
            'user_name': 'TestName',
        }
        response = requests.post("http://127.0.0.1:8000/form/get_form/", params=data)
        self.assertEqual(response.content, b'QuestionCreateForm')

    def test_request4(self):
        # ни одна из форм не подходит
        data = {
            'contact_phone': '+7 111 111 11 11',
            'user_name': 'TestName',
        }
        response = requests.post("http://127.0.0.1:8000/form/get_form/", params=data)
        self.assertEqual(response.content, b'{"contact_phone": "phone", "user_name": "text"}')

    def test_request5(self):
        # пустая дата
        data = {}
        response = requests.post("http://127.0.0.1:8000/form/get_form/", params=data)
        self.assertEqual(response.content, b'{}')
