a = int(input("Enter a number: "))
ts = 0

for i in range(1, a + 1):
    
    ts += i

print(f"The sum of the first {a} natural numbers is: {ts}")