import requests
import unittest

URL = 'http://0.0.0.0:5000/rest'


class TestRest(unittest.TestCase):
    def test_create_department(self):
        r = requests.post(URL + '/departments', json={'department_name': 'Test_create_department'})
        self.assertEqual(r.status_code, 201)

        r = requests.get(URL + '/departments/Test_create_department')
        self.assertEqual(r.text.strip(), '"Test_create_department"')

        requests.delete(URL + '/departments/Test_create_department')

    def test_remove_department(self):
        requests.post(URL + '/departments', json={'department_name': 'Test_remove_department'})

        r = requests.delete(URL + '/departments/Test_remove_department')
        self.assertEqual(r.status_code, 204)

    def test_create_employee(self):
        requests.post(URL + '/departments', json={'department_name': 'Test'})
        r = requests.post(URL + '/employees', json={'employee_name': 'Test_employee_create',
                                                    'employee_salary': '3600',
                                                    'employee_birth': '2000-11-13',
                                                    'employee_department': 'Test'})
        self.assertEqual(r.status_code, 201)
        requests.delete(URL + '/departments/Test')

    def test_get_employees(self):
        requests.post(URL + '/departments', json={'department_name': 'Test'})
        requests.post(URL + '/employees', json={'employee_name': 'Test_employee_create',
                                                'employee_salary': '3600',
                                                'employee_birth': '2000-11-13',
                                                'employee_department': 'Test'})
        requests.post(URL + '/employees', json={'employee_name': 'Test_employee_create_1',
                                                'employee_salary': '3600',
                                                'employee_birth': '2000-11-13',
                                                'employee_department': 'Test'})
        r = requests.get(URL + '/employees')
        counter = 0
        for i in r.json():
            if i['Name'] in ['Test_employee_create', 'Test_employee_create_1']:
                counter += 1
        self.assertEqual(counter, 2)
        requests.delete(URL + '/departments/Test')

    def test_remove_employee(self):
        requests.post(URL + '/departments', json={'department_name': 'Test'})
        requests.post(URL + '/employees', json={'employee_name': 'Test_employee_remove',
                                                'employee_salary': '3600',
                                                'employee_birth': '2000-11-13',
                                                'employee_department': 'Test'})
        employees = requests.get(URL + '/employees')
        for i in employees.json():
            if i['Name'] == 'Test_employee_remove':
                r = requests.delete(URL + '/employees/'+str(i['id']))
                self.assertEqual(r.status_code, 204)
                break
        else:
            self.assertTrue(False)
        requests.delete(URL + '/departments/Test')


if __name__ == '__main__':
    unittest.main()
