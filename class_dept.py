class Employee:
    pass


class Department:
    dept_name = ""
    employees = []  
    def list_employees(self):
        print(f"Employees in {self.dept_name}:")
        for emp in self.employees:
            print(f"- {emp.name}")


emp1 = Employee() 
emp1.name = "Aditya"
emp2= Employee() 
emp2.name="Rakshita"
emp3= Employee() 
emp3.name="Abdusammad"
dept = Department()
dept.dept_name = "Engineering"


dept.employees.append(emp1)
dept.employees.append(emp2)
dept.employees.append(emp3)

dept.list_employees()