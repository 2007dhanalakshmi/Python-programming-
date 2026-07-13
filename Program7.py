# Count Even and Odd Numbers

m = int(input("Enter the Maximum Value: "))

event = 0
oddt = 0

for number in range(1, m + 1):

    # Check even
    if number % 2 == 0:
        event += 1

    # Otherwise odd
    else:
        oddt += 1

print("Total Even Numbers =", event)
print("Total Odd Numbers =", oddt)

Total Even Numbers = 5
Total Odd Numbers = 5
