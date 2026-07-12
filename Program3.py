# Program 3 - Total Marks, Average and Grade

n = int(input("Enter the number of subjects: "))
tot = 0

for i in range(1, n + 1):
    print("Enter mark", i, ":")
    m = int(input())
    tot = tot + m

print("Total Marks =", tot)

avg = tot / n
print("Average =", avg)

if avg >= 80:
    print("Grade A")
elif avg >= 70:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
elif avg >= 40:
    print("Grade D")
else:
    print("Grade E")
