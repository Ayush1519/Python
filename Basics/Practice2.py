bal = int(input("Enter balance: "))

wd = int(input("Enter withdrawal amount: "))

while not (wd % 100 == 0 or wd % 500 == 0):
    wd = int(input("Enter withdrawal amount (multiple of 100 or 500): "))

if wd < 0:
    print("Invalid amount")
elif wd > bal:
    print("Insufficient balance")
else:
    print("Withdrawal successful. Remaining balance:", bal - wd)

----------------------------------------------------------------------------------------------------------------------------------------------------------
unit = float(input("Enter unit: "))
bill = 0

if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = 100 * 5 + (unit - 100) * 8
else:
    bill = 100 * 5 + 100 * 8 + (unit - 200) * 10

gst = bill * 0.05
total = bill + gst

print("Total bill (with GST):", total)
