def generate_emp_id(dept_code, number):
    return f"{dept_code}-{number:03d}"

def is_eligible_for_bonus(years, rating):
    return years >= 2 and rating >= 4.0

def calculate_attendance_percent(present_days, total_days):
    return (present_days / total_days) * 100