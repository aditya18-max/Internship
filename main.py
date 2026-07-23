import salary_utils

basic_salary = float(input("Enter basic salary: "))

hra = salary_utils.calculate_hra(basic_salary)
net_salary = salary_utils.calculate_net_salary(basic_salary)

print("\n--- Salary ---")
print(f"Basic Salary : {basic_salary:,.2f}")
print(f"HRA          : {hra:,.2f}")
print(f"Net Salary   : {net_salary:,.2f}")