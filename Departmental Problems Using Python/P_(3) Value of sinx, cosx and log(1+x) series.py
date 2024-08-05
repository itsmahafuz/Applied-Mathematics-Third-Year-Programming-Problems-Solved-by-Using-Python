# DATE : August 6th, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Calculate the value of sinx ,cosx and log(1+x) using its series for some given x.

import math

# Function to calculate sine using the series expansion
def SineFun(x, n):
    sum = x  # Initialize sum with the first term of the series
    y = (7 * 180 * x) / 22  # Convert x back to degrees for display purposes
    term = x  # The first term is just x

    # Loop to calculate the series up to n terms
    for i in range(1, n):
        term *= -x**2 / ((2 * i) * (2 * i + 1))  # Calculate the next term
        sum += term  # Add the term to the sum

    # Print the result with formatted output
    print("\nThe value of sin({:.2f}) is: {:.5f}".format(y, sum))
    
# Function to calculate cosine using the series expansion
def CosineFun(x,n):
    sum = 1  # Initialize sum with the first term of the series
    y = (7 * 180 * x) / 22  # Convert x back to degrees for display purposes
    fact=1
    
    # Loop to calculate the series up to n terms
    for i in range (1,n):
        fact*=(2*i)*(2*i-1)
        sum+=(-1)**i*x**(2*i)/fact
    print("\nThe value of sin({:.2f}) is : {:.5f}".format(y,sum))


def LogFun(y, n):
    x = 1 + y
    
    # Calculate v used in the series approximation
    v = (x - 1) / (x + 1)
    sum_ln = 0.0
    
    # Use the series expansion for ln(1+x)
    for i in range(n):
        term = (v**(2*i + 1)) / (2*i + 1)
        sum_ln += term
    
    # Calculate the value of ln(1+x)
    ln_value = 2 * sum_ln

    # Convert ln(1+x) to log10(1+x)
    log10_value = ln_value / math.log(10)
    
    # Calculate the actual value of log10(1+x)
    actual_value = math.log10(x)
    
    # Calculate the error
    error = abs(actual_value - log10_value)
    
    # Print the results
    print(f"\nThe actual value of log10(1+y) using the standard library: {actual_value:.10f}")
    print(f"\nError: {error:.10f}")
    print(f"\nThe value of log10(1 + {y}) = {log10_value:.10f}")
      
    
    
    
while True:
    # Input for the value of x and converting it from degrees to radians
    x = float(input("\nEnter the value of x for sin(x)  and cos(x) series (in degrees): "))
    x = math.radians(x)  # Use math.radians to convert degrees to radians
    # Input for the number of terms to calculate in the series
    
    c=float(input("\nEnter the value of x for log(1+x) series : "))
    
    n = int(input("\nEnter the number of terms that you want to calculate: "))
    
    # Call the function to calculate sine
    SineFun(x, n)
    
    # Call the function to calculate cosine
    CosineFun(x, n)
    
    # Call the function to calculate log(1+x)
    LogFun(c, n)
    
    
    # Prompt user to check for another value
    print("\nDo you want to check for another value of x and n? ")
    choice = input("If yes, press y/Y. For no, press n/N: ")
    if choice.lower() != 'y':
        break

    