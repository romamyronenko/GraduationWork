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
    """Show list of departments."""
    departments_list = ra.Departments().get()
    department = ra.Department()
    return render_template('departments.html',
                           departments=[{'Name': i['Name'],
                                         'Count of employees': department.get_count_of_employees(i['Name']),
                                         'Avg salary': department.get_avg_salary(i['Name'])}
                                        for i in departments_list])


@app.route('/add/department', methods=['GET', 'POST'])
def add_department_page():
    """Form to add new department."""
    if request.method == 'POST':
        # print(ra.Departments().post())
        # print(request.form.get('department_name'))
        if ra.Departments().post() == (request.form.get('department_name'), 201):
            return redirect('../../departments')
        print(111)
    return render_template('add_department.html')


@app.route('/employees')
def employees_page():
    """Show list of employee."""
    employees_list = ra.Employees().get()
    return render_template('employees.html',
                           departments=[{'id': i['id'],
                                         'Name': i['Name'],
                                         'Birth': i['Birth'],
                                         'Salary': i['Salary'],
                                         'Department': i['Department']}
                                        for i in employees_list])


@app.route('/add/employee', methods=['GET', 'POST'])
def add_employee_page():
    """Form to add new employee."""
    if request.method == 'POST':
        if ra.Employees().post() == (request.form.get('employee_name'), 201):
            return redirect('../../employees')
    departments_list = [i['Name'] for i in ra.Departments().get()]
    return render_template('add_employee.html', departments=departments_list)


@app.route('/employees/<int:employee_id>/remove', methods=['GET', 'POST'])
def remove_employee_page(employee_id):
    """Show form to confirm remove employee."""
    employee = ra.Employee()
    if request.method == 'POST':
        employee.delete(employee_id)
        return redirect('../../employees')
    return render_template('remove_employee.html',
                           employee_name=employee.get(employee_id)[0]['Name'])


@app.route('/employees/<int:employee_id>/edit', methods=['GET', 'POST'])
def edit_employee_page(employee_id):
    """Show form to edit employee."""
    if request.method == "POST":
        ra.Employee().put(employee_id)
        return redirect('../../employees')
    employee = ra.Employee().get(employee_id)[0]
    departments_list = [i['Name'] for i in ra.Departments().get()]
    return render_template('add_employee.html',
                           name=employee['Name'],
                           salary=employee['Salary'],
                           birth=employee['Date'],
                           department=employee['Department'],
                           departments=departments_list)


api.add_resource(ra.Departments, '/rest/departments')
api.add_resource(ra.Department, '/rest/departments/<string:department_name>')
api.add_resource(ra.Employees, '/rest/employees')
api.add_resource(ra.Employee, '/rest/employees/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1:5000')
