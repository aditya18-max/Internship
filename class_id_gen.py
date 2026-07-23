class Employee:
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")

    @staticmethod
    def generate_id(dept_code, number):
        return f"{dept_code.upper()}-{number}"


id_1 = Employee.generate_id("eng", 14)
id_2 = Employee.generate_id("hr", 5)
id_3 = Employee.generate_id("mkt", 102)

print("--- Generated New Hire IDs ---")
print(f"New Hire 1 ID: {id_1}")
print(f"New Hire 2 ID: {id_2}")
print(f"New Hire 3 ID: {id_3}")