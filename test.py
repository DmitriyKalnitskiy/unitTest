import unittest
from app import app
import requests

class TestApp(unittest.TestCase):

    # проверка на успешность запроса
    def test_index_page_availability(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_submission(self):

        response = self.app.post('/submit', data={
            'name': 'Vova',
            'SurName': 'Petrov',
            'age': '35',
            'gender': 'male',
            'feedback': 'Very well!'
        })

        # проверка на сохранение инф. в файл
        with open("responses.txt", "r") as file:
            content = file.read()
            self.assertIn('Имя: Vova', content)
            self.assertIn('Фамилия: Petrov', content)
            self.assertIn('Возраст: 35', content)
            self.assertIn('Пол: male', content)
            self.assertIn('Отзыв: Very well!', content)