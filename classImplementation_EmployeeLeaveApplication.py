#Program to manage the leave application of an employee

class Employee:
    def __init__(self,empno,empname,leaves):
        self.empno =empno
        self.empname =empname
        self.leaves = leaves


class Company:
    def __init__(self, cname, emp_list):
        self.cname =cname
        self.emps = emp_list

    def display_leave(self,empno,leave_type):
        for emp in self.emps:
            if empno == emp.empno:
                print(emp.leaves[leave_type])

    def leave_application(self,empno,leave_type,noofleaves):
        for emp in self.emps:
            if empno == emp.empno:
                if emp.leaves[leave_type] >= noofleaves:
                    return "Granted"
        return "Rejected"


if __name__ =='__main__':
    n = int(input())
    emps = []
    c= Company("ABC",emps)
    for i in range(n):
        leaves = {}
        eno = int(input())
        ename = input()
        leaves['CL'] = int(input())
        leaves['EL'] = int(input())
        leaves['SL'] = int(input())

        e = Employee(eno,ename,leaves)
        c.emps.append(e)
    empno = int(input())
    Itype =input()
    nol = int(input())
    print(c.display_leave(empno, Itype))
    print(c.leave_application(empno,Itype,nol))