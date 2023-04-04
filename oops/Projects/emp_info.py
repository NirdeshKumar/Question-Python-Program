
"""
1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary,
and emp_department and methods like calculate_emp_salary, emp_assign_department,
and print_employee_details.

Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

==>Use 'assign_department' method to change the department of an employee.

==>Use 'print_employee_details' method to print the details of an employee.

==>Use 'calculate_emp_salary' method takes two arguments:
salary and hours_worked,which is the number of hours worked by the employee.
If the number of hours worked is more than 50,the method computes overtime -
and adds it to the salary. Overtime is calculated as following formula:

overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))

"""




class Employee():
    def __init__(self):
        self.__name=input("enter a Name: ")
        self.__emp_id=input("enter a employee id: ")
        self.__salary=int(input("enter your salary: "))
        self.__emp_dept=input("enter your department: ")
    def sal_cal(self):
        self._hour_work=int(input("enter a worked hour: "))
        if(self._hour_work>50):
            o=self._hour_work-50
            o_time=(o*(self.__salary/50))
            self.__salary=self.__salary+o_time
            print("Over time Work Amount: ",o_time)
            print("total salary: ",self.__salary)
        else:
            print("total salary: ",self.__salary)
    def change_dept(self):
        user=input("If you want to chane the department, New department Name : ")
        self.__emp_dept=user
        print("New department Name: ",self.__emp_dept)
            
    def emp_detail(self):
        user=input("enter your emp_id: ")
        if(self.__emp_id==user):
            print(f"Employee Details\nName: {self.__name}\nEmploye ID: {self.__emp_id}\nSalary: {self.__salary}\nEmploye Department: {self.__emp_dept}")
    
        else:
            print("Invalid ID")
