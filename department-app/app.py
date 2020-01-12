from flask import Flask, render_template, redirect, g, request
from flask_restful import Api
import rest.rest_app as ra

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return redirect('/departments')


@app.route('/departments')
def departments_page():
    departments_list = ra.Departments().get()
    return render_template('departments.html',
                           departments=[{'Name': i['Name'],
                                         'Count of employees': ra.Department().get_count_of_employees(i['Name']),
                                         'Avg salary': ra.Department().get_avg_salary(i['Name'])}
                                        for i in departments_list])


@app.route('/employees')
def employees_page():
    employees_list = ra.Employees().get()
    return render_template('employees.html',
                           departments=[{'Name': i['Name'],
                                         'Birth': i['Birth'],
                                         'Salary': i['Salary'],
                                         'Department': i['Department']}
                                        for i in employees_list])


@app.route('/add/employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        print(request.form.get('Name'))
        print(request.form.get('Birth'))
        print(request.form.get('Department'))
        print(request.form.get('Salary'))
    departments_list = [i['Name'] for i in ra.Departments().get()]
    return render_template('add_employee.html', departments=departments_list)


api.add_resource(ra.Departments, '/rest/departments')
api.add_resource(ra.Department, '/rest/departments/<string:department_name>')
api.add_resource(ra.Employees, '/rest/employees')
api.add_resource(ra.Employee, '/rest/employees/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1:5000')
