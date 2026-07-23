class Payroll:

    def calculate_net_salary(self):
        hra = 0.40 * self.basic_salary
        da = 0.10 * self.basic_salary
        deductions = 0.05 * self.basic_salary

        net_salary = self.basic_salary + hra + da - deductions
        return net_salary


# Create object
pay = Payroll()

# Assign basic salary using dot notation
pay.basic_salary = int(input("Enter the salary:"))
# Calculate and print net salary
net_salary = pay.calculate_net_salary()
print(f"Net Salary: {net_salary}")