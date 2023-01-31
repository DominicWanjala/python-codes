# a program to allow east african member to vote.
East_africa = ["kenyan", "ugandan", "tanzanian"]
age = int(input("Enter your age:"))
nationality = input("Enter your nation:").lower()
if age >= 18 and nationality in East_africa:

    print("eligible to vote.")

else:
    print("Unfortunately, you are not allowed to vote.")
