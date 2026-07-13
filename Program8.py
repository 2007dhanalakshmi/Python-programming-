# Program to Reverse a String Word by Word

class stringc:

    # Function to reverse words
    def reversew(self, s):
        return ' '.join(reversed(s.split()))

# Read input
s = input("Enter the String: ")

# Display reversed string
print(stringc().reversew(s))

Enter the String:
welcome to python program

program python to welcome
