#to be modified laters
print("Prices for Today's BlockBuster")

age = range(1, 100)
age = int(input("Enter age: "))
if age < 3:
    print("Free tickets")
elif 3 <= age < 12:
    print("$10 ticket")
elif age > 12:
    print("$15 ticket")
else:
    print("Enter valid age")