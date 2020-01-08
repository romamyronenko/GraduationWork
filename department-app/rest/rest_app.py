from flask import Flask
from flask_restful import Api, Resource
import service


def wrapper(f):
    def connect_db(*args, **kwargs):
        sentinel = object()

        g = f.__globals__
        old_value = dict()
        old_value['db'] = g.get('db', sentinel)

        g['db'] = service.db.DataBase(user='debian-sys-maint',
                                      password='PggWbsvEVgDZUYar',
                                      host='127.0.0.1',
                                      database='roma')

        res = f(*args, **kwargs)
        g['db'].close()

        if old_value is sentinel:
            del g['db']
        else:
            g['db'] = old_value
        return res
    return connect_db


app = Flask(__name__)
api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('department_name')
# parser.add_argument('name')


class Department(Resource):
    """
    Show a single department and lets you delete or edit a department.
    """
    @wrapper
    def get(self, department_name):
        """Return department data."""
        return db.get_department(department_name)

    @wrapper
    def delete(self, department_name):
        """Remove department from list."""
        db.remove_department(department_name)
        return '', 204

    @wrapper
    def put(self, department_name):
        """Add department to list."""
        db.edit_department(department_name, 'new_name')
        return '', 200


class Departments(Resource):
    """
    Show a list of departments.
    """
    @wrapper
    def get(self):
        """Return list of departments."""
        departments = db.get_departments()
        return [{'Name': name} for (name,) in departments]

    @wrapper
    def post(self):
        pass


class Employee(Resource):
    @wrapper
    def get(self, employee_id):
        """Return employee data."""
        employee = db.get_employee(employee_id)
        return [{'id': employee[0],
                 'Name': employee[1],
                 'Department': employee[2],
                 'Date': str(employee[3]),
                 'Salary': employee[4]}]

    @wrapper
    def delete(self, employee_id):
        """Remove employee from list."""
        db.delete_employee(employee_id)
        return '',  204

    @wrapper
    def put(self, employee_id):
        """Add employee to list."""
        db.edit_employee(employee_id, 'New_name', '2-2-1997', '2300', 'Finance')
        return '', 200


class Employees(Resource):
    """
    Show a list of employees.
    """
    @wrapper
    def get(self):
        """Return list of employee."""
        employees = db.get_employees()
        return [{'id': employee_id,
                 'Name': name,
                 'Department': department,
                 'Birth': str(birth),
                 'Salary': salary} for (employee_id, name, department, birth, salary) in employees]

    @wrapper
    def post(self):
        pass


api.add_resource(Departments, '/departments')
api.add_resource(Department, '/departments/<department_name>')
api.add_resource(Employees, '/employees')
api.add_resource(Employee, '/employees/<employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
