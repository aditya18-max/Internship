class Employee:
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")


class Manager(Employee):
    def display_info(self):
        # Call the parent method to print base details
        super().display_info()
        # Print the extra team_size attribute
        print(f"Team Size  : {self.team_size}")

mgr = Manager()

mgr.name = input("Enter Manager Name: ")
mgr.emp_id = input("Enter Employee ID: ")
mgr.department = input("Enter Department: ")
mgr.team_size = int(input("Enter Team Size: "))

print("\n--- Manager Details ---")
mgr.display_info()