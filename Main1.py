import hr_utils

emp_id = hr_utils.generate_emp_id("ENG", 14)
bonus_status = hr_utils.is_eligible_for_bonus(3, 4.5)
attendance = hr_utils.calculate_attendance_percent(22, 24)

print("Generated ID:", emp_id)
print("Eligible for Bonus:", bonus_status)
print(f"Attendance: {attendance:.2f}%")