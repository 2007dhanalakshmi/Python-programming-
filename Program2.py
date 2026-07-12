# Program 2 - Pattern using Nested For Loop

r = int(input("Enter the rows you want to generate the series: "))

for i in range(1, r + 1):
    for j in range(0, r - i + 1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print()

for i in range(r - 1, 0, -1):
    for j in range(0, r - i + 1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print()
  
