age = int(input("Enter age: "))

day = input("Enter day: ")

price = 12 if age <= 19 else 8

print("Final price will be: ",price)

if day == "wed":
    price = price - 2
    
print("Discounted Price: ",price)