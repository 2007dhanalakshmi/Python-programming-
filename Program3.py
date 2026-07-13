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

output:
Enter the number of subject marks:5
Enter the 1 mark:10
Enter the 2 mark:90
Enter the 3 mark:80
Enter the 4 mark:70
Enter the 5 mark:80
Total marks=330
Average of marks=66.0
Grade C
