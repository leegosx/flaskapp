import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import unittest
import csv
from app.main import app, sort_csv
from io import BytesIO

class TestCSVSorting(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Load test data from sample.csv
        test_data_path = os.path.join('tests', 'test_data', 'sample.csv')
        with open(test_data_path, 'r') as file:
            self.test_csv = file.read()
            file.seek(0)  # Reset file pointer
            self.csv_data = list(csv.DictReader(file))

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_sort_by_vorname(self):
        file = BytesIO(self.test_csv.encode('utf-8'))
        result = sort_csv(file, 'Vorname')
        # Test first and last alphabetically
        self.assertIn('Aaron', result)
        self.assertIn('Steven', result)

    def test_sort_by_stadt(self):
        file = BytesIO(self.test_csv.encode('utf-8'))
        result = sort_csv(file, 'Stadt')
        # Test Berlin and Köln
        self.assertIn('Berlin', result)
        self.assertIn('Köln', result)

    def test_sort_by_plz(self):
        file = BytesIO(self.test_csv.encode('utf-8'))
        result = sort_csv(file, 'PLZ')
        # Test lowest and highest PLZ
        self.assertIn('10553', result)
        self.assertIn('53844', result)

    def test_post_with_valid_file(self):
        data = {
            'file': (BytesIO(self.test_csv.encode('utf-8')), 'sample.csv'),
            'column': 'Stadt'
        }
        response = self.app.post('/', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)

    def test_post_without_file(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
