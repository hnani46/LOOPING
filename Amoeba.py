.....
The environmental eco club has discovered a new Amoeba that grows in the order of a Fibonacci series every month. They are exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular time instant. If a particular month’s index is given, write a  program to displays the amoeba’s size……???. For Example, The size of the amoeba on month 1, 2, 3, 4, 5, 6, ..will be 0, 1, 1, 2, 3, 5, 8 respectively.
....
Sample Input:
7
Sample Output:
8
....
Ans:
n=int(input())
a=0
b=1
for i in range (3,n+1):
	c=a+b
	a=b
	b=c
print (c)
code:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        
    return b

# Example usage:
try:
    month = int(input("Enter the month index to get the amoeba's size: "))
    size = fibonacci(month)
    print(f"The size of the amoeba in month {month} is: {size}")
except ValueError:
    print("Please enter a valid integer.")
....
output:
Enter the month index to get the amoeba's size: 5
The size of the amoeba in month 5 is: 3
​

