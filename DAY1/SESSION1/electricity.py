unit=float(input("Enter units consumed: "))
bill=0
if unit <= 100:
   bill = unit*1.50
elif unit <= 200:
   bill=(100*1.50)+((100*1.50)+((unit-200)*4.00))
else:
   bill = (100*1.50)+(100*2.50)+((unit-200)*4.00)
   print("total electricity bill = Rs", format(bill, ".2f" ))