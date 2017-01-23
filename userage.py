from datetime import datetime

user_name=input("Enter your name:\n")
user_age=int(input("Enter your age:\n"))

hundrd=int((100-user_age)+datetime.now().year)
print("Year when u will turn 100 is: ",hundrd)