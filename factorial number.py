.....
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
....
Sample Input:
6
Sample Output:
Yes
...
code;
def is_factorial_number(n):
    if n < 0:
        return False  # Factorials are non-negative
    
    factorial = 1
    i = 1
    
    while factorial < n:
        i += 1
        factorial *= i
    
    return factorial == n

# Example usage:
n = int(input("Enter a number to check if it's a factorial number: "))
if is_factorial_number(n):
    print(f"{n} is a factorial number.")
else:
    print(f"{n} is not a factorial number.")
....
output:
Enter a number to check if it's a factorial number: 6
6 is a factorial number.
