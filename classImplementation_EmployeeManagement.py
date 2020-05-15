#Employee management for incrementing salary for particular
#job role only, implemented using multiple classes

class Employee:
    def __init__(self, emp_id, emp_name, emp_role, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary


    def increase_salary(self, percentage):
        self.emp_salary = int(self.emp_salary) + (int(self.emp_salary) * percentage)

class Organisation():

    def __init__(self, org_name, emp_list):
        self.org_name =org_name
        self.emp_list = emp_list

    def calculate_increment(self, emp_role, increment):
        emp_res =[]
        for emp in self.emp_list:
            if emp_role == emp.emp_role:
                emp.increase_salary(increment)
                emp_res.append(emp)
        return emp_res


if __name__ =='__main__':
    emp_list =[]
    count = int(input())
    for i in range(count):
        eid = int(input())
        name = input()
        role = input()
        salary = input()
        emp_list.append(Employee(eid,name,role,salary))
    o = Organisation("XYZ Corp", emp_list)
    inp_role = input()
    inp_percentage = int(input())
    inp_percentage = inp_percentage * 0.01
    result = o.calculate_increment(inp_role,inp_percentage)
    if len(result) != 0:
        for emp in result:
            print(emp.emp_name, '\t', emp.emp_salary)
    else:
        print("No employee found with given role")