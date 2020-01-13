import requests
import unittest

URL = 'http://127.0.0.1:5000/rest'


class TestRest(unittest.TestCase):
    def test_create_department(self):
        r = requests.post(URL+'/departments', json={'department_name': 'Test_create_department'})
        self.assertEqual(r.status_code, 201)

        r = requests.get(URL + '/departments/Test_create_department')
        self.assertEqual(r.text.strip(), '"Test_create_department"')

        requests.delete(URL+'/departments/Test_create_department')

    def test_create_employee(self):
        r = requests.post(URL+'/employees', json={})


if __name__ == '__main__':
    unittest.main()
