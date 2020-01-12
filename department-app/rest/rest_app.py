from flask_restful import Resource, reqparse
import service


def wrapper(f):
    """Method that create connection to database and close it after usage."""
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


parser = reqparse.RequestParser()
parser.add_argument('department_name')
parser.add_argument('employee_name')
parser.add_argument('employee_birth')
parser.add_argument('employee_salary')
parser.add_argument('employee_department')


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
        """Edit department data."""
        args = parser.parse_args()
        db.edit_department(department_name, args['department_name'])
        return '', 200

    @wrapper
    def get_count_of_employees(self, department_name):
        return db.get_count_of_employees(department_name)

    @wrapper
    def get_employees(self, department_name):
        return [{
            'id': i[0],
            'Name': i[1],
            'Department': i[2],
            'Date': i[3],
            'Salary': i[4],
        }for i in db.get_employees_by_department(department_name)]

    @wrapper
    def get_avg_salary(self, department_name):
        return db.get_avg_salary(department_name)


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
        """Add new department."""
        args = parser.parse_args()
        db.create_department(args['department_name'])
        return args['department_name'], 201


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
        db.remove_employee(employee_id)
        return '', 204

    @wrapper
    def put(self, employee_id):
        """Edit employee data."""
        args = parser.parse_args()
        db.edit_employee(employee_id,
                         args['employee_name'],
                         args['employee_birth'],
                         args['employee_salary'],
                         args['employee_department'])
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
        """Add new employee."""
        args = parser.parse_args()
        db.create_employee(name=args['employee_name'],
                           department=args['employee_department'],
                           salary=args['employee_salary'],
                           birth=args['employee_birth'])
        return args['employee_name'], 201
