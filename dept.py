depts = ["Gaming", "Coding", "Testing", "Developing", "HR", "Designing", "Designing", "Sales"]
names = ["Aditya", "Rakshita", "Rihan", "Keerti", "Abdusammad", "Ranjita", "Priyanka", "Namrata"]

grouped = {}
i = 0 
for dept in depts:
    name = names[i]
    
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(name)
    
    i = i + 1  

# Print each item line by line
for dept in grouped:
    print(dept, ":", grouped[dept])