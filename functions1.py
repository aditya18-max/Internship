def percentage(score):
    if(score>=90):
        print("A")
    elif(score>=80):
        print("B")
    elif(score>=70):
        print("C")
    elif(score>=60):
        print("D")
    elif(score>=50):
        print("E") 
    elif(score>=40):
        print("F")
    else:
        print("Go to Home and sleep!!!!!!!")

score=int(input("Enter your percentage:"))
percentage(score)   