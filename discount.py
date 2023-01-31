# A program to assign discount in a purchase
purchase=float(input("Enter purchase:"))
if purchase > 1000:
    discount = purchase * 0.05
    print("Your discount is",discount)
else:
    print("no discount")