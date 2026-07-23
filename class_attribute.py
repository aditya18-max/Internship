class Employee:
    company_name = "Digital Dream Institute"


emp1 = Employee()
emp1.emp_id = "EMP101"
emp1.name = "Aditya"

emp2 = Employee()
emp2.emp_id = "EMP102"
emp2.name = "RRK"

print(f"{emp1.name} works at {emp1.company_name}")
print(f"{emp2.name} works at {emp2.company_name}")

print(f"Company Name: {Employee.company_name}")