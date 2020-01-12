import requests
import unittest

URL = 'http://127.0.0.1:5000/rest'


class TestRest(unittest.TestCase):

    def test_crud_department(self):
        r = requests.post(URL+'/departments', json={'department_name': 'Test'})
        self.assertEqual(r.status_code, 201)

        r = requests.get(URL + '/departments/Test')
        self.assertEqual(r.text.strip(), '"Test"')

        requests.put(URL+'/departments/Test', json={'department_name': 'Test_update'})
        self.assertEqual(requests.get(URL + '/departments/Test_update').text.strip(), '"Test_update"')

        r = requests.delete(URL+'/departments/Test_update')
        self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    unittest.main()
