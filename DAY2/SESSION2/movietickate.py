day = int(input("Enter day (1-7): "))
time = int(input("Enter show time: "))
age = int(input("Enter age: "))
seat = int(input("Seat (1-Regular, 2-Premium, 3-Recliner): "))

price = 200
print("Base Price:", price)
if day >= 1 and day <= 4:
    discount = price * 0.20
    price -= discount
    print("Weekday Discount:", discount)
else:
    print("Weekday Discount: 0")
if age < 12 or age > 60:
    discount = price * 0.30
    price -= discount
    print("Age Discount:", discount)
else:
    print("Age Discount: 0")
if seat == 1:
    surcharge = 0
elif seat == 2:
    surcharge = 100
elif seat == 3:
    surcharge = 250

price += surcharge
print("Surcharge:", surcharge)
if price > 500:
    gst = price * 0.18
else:
    gst = price * 0.12
final = price + gst
print("GST:", gst)
print("Final Price:", final)