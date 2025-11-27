import sys

if len(sys.argv) == 2:
    units = float(sys.argv[1])
    print("User provided units:")
else:
    units = 100
    print("No input given — using default units = 100:")

rate = 5
bill = units * rate

print("Units Consumed:", units)
print("Rate per Unit: ₹5")
print("Total Bill: ₹", bill)
