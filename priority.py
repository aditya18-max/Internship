
tasks=["Gaming","Editing","singing","Abc","xyz"]
print("Tasks: are",tasks)
priority=int(input("Enter task priority (e.g., 1, 2, 3, 4): "))
if priority == 1:
    label = "Urgent"
elif priority == 2 or priority == 3:
    label = "Normal"
else:
    label = "Low"

print("Task Label:", label)