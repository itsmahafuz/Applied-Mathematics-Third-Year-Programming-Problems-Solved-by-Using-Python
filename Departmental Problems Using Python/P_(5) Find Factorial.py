#  DATE : August 3rd,2024
#  MD MAHAFUZUR RAHMAN
#  Roll:2110428176
#  Department of Applied Mathematics
#  University Of Rajshahi.
#  LinkedIn : https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
#  GitHub : https://github.com/itsmahafuz

# Program to find factorial of any given number.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

while True:
    print("\n")
    n=int(input("Enter a number to find it's factorial:"))
    print("The factorial of the given number is : ",factorial(n))
    
    print("\n")
    print("Do you want to check for another number?")
    iter=(input("Enter  (y/Y) for Yes and (n/N) for No : "))
    if iter.lower() != 'y':
        break