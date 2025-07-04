age = int(input("Enter Age: "))
day = input("Enter day: ")

if age < 19:
    print("Price for children is $8")
    
    if day == "wed":
        print("discounted price is $6")

elif age>= 19:
    print("Price for Adults is $12")
    
    if day == "wed":
        print("discounted price is $10")    