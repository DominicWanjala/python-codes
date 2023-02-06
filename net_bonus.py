#A program to output the net bonus amount.
x=int(input("Enter your salary"))
y=int(input("enter the year of service"))

if (y>10):
    net=(x*0.1)
    print("Net bonus amount=",net)
elif (y>=6 and y<=10):
    net=(x*0.08)
    print("Net bonus amount=",net)
else:
     net=(x*0.05)
     print("Net bonus amount=",net)