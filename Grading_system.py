#A program to output the grading system.
x=int(input("Enter your score in unit 1"))
y=int(input("Enter your score in unit 2"))
z=int(input("Enter your score in unit 3"))
avg=(x+y+z)/3
if (avg>=70 and avg <= 100):
    print("Your grade is A")
elif (avg>=70 and avg <= 100):
    print("Your grade is B")
elif (avg>=50 and avg <= 59):
    print("Your grade is C")
elif (avg>=40 and avg <= 49):
    print("Your grade is D")
else:
     print("Fail")