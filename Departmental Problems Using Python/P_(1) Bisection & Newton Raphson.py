# Date: August 5th,2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Solve suppressed cubic or transcendental functions by Bisection
# and Newton-Raphson methods.

# Function to evaluate the given cubic function f(x) = x^3 - 2x - 5
def funct(x):
    return x**3 - 2*x - 5

# Function to evaluate the derivative of the given function f'(x) = 3x^2 - 2
def ffunct(x):
    return 3*x**2 - 2

# Function to find the root of the function using the Bisection method
def Bisection(a, b, tol):
    # Check if the initial interval [a, b] is valid
    if funct(a) * funct(b) >= 0:
        print("\nThere is no root between this given interval.\n")
    else:
        # Calculate the midpoint of the interval
        c = (a + b) / 2
        # Check if the midpoint is the root
        if funct(c) == 0:
            print("\nThe root of the equation between the given interval is: ", round(c, 9))
        else:
            # Continue the bisection process until the interval size is smaller than the tolerance
            while abs(a - b) >= tol:
                c = (a + b) / 2
                # Check which sub-interval contains the root
                if funct(a) * funct(c) < 0:
                    b = c
                elif funct(c) * funct(b) < 0:
                    a = c
            # Print the result
            print("\n***** According to Bisection method *****")  
            print("\nThe root of the equation between the given interval is: ", round(c, 9), "\n")
            
# Function to find the root of the function using the Newton-Raphson method
def NewtonRaphson(x1, tol):
    x0 = 0  # Initialize the previous guess
    i = 1   # Initialize the iteration counter
    print("\n***** According to Newton-Raphson Method *****")
    
    # Continue the Newton-Raphson process until the difference between consecutive guesses is smaller than the tolerance
    while abs(x1 - x0) >= tol:
        x0 = x1
        # Check for a zero derivative to avoid division by zero
        if ffunct(x0) == 0:
            print("\nMathematical error!!")
            return
        # Update the guess using the Newton-Raphson formula
        x1 = x0 - funct(x0) / ffunct(x0)
        print("\nAt step-", i, " x", i, "=", x1)
        i += 1
    
    # Print the result
    print("\nThe root of the equation is: ", round(x1,9))
    print("\nNumber of iterations: ", i - 1)


while True:
    # Input for the initial interval [a, b] for the Bisection method
    input_line = input("Enter the initial interval [a, b] for Bisection method (use space between the interval): ")
    a, b = map(float, input_line.split())

    # Input for the initial guess for the Newton-Raphson method
    ig = float(input("Enter the initial guess for the Newton-Raphson Method: "))
    # Input for the tolerance level
    tol = float(input("Enter the tolerance: "))

    # Call the Bisection method
    Bisection(a, b, tol)
    # Call the Newton-Raphson method
    NewtonRaphson(ig, tol)
    
    print("\nDo you want to check for another interval? ")
    choice=input("If yes the press y/Y and for no press n/N : ")
    if choice.lower() !='y':
        break

