.....
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
...
Sample Input:
791
Sample Output:
Trendy Number
...
code:
def is_trendy_number(num):
    # Check if the number is a three-digit number
    if 100 <= num <= 999:
        # Convert the number to a string to access the digits
        num_str = str(num)
        middle_digit = int(num_str[1])  # Get the middle digit
        
        # Check if the middle digit is divisible by 3
        return middle_digit % 3 == 0
    else:
        return False

# Example usage:
try:
    number = int(input("Enter a three-digit number to check if it's trendy: "))
    if is_trendy_number(number):
        print(f"{number} is a trendy number.")
    else:
        print(f"{number} is not a trendy number.")
except ValueError:
    print("Please enter a valid integer.")
....
output:
Enter a three-digit number to check if it's trendy: 234
234 is a trendy number.
