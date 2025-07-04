user_age = int(input("Enter your age: "))

if user_age < 13:
    print("Child")
    
elif user_age >= 13 and user_age <= 19:
    print("Teenager")
    
elif user_age > 19 and user_age <= 59:
    print("Adult")
    
elif user_age > 60:
    print("Senior")    