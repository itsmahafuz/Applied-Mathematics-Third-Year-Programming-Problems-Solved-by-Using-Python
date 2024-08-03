# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to find the largest and smallest number that can be formed using
# digits of a given number.

# Function to sort a list of characters in ascending order
def ascending(list, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            # Swap if the element found is greater than the next element
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

# Function to sort a list of characters in descending order
def descending(list, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            # Swap if the element found is less than the next element
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

# Main loop to keep the program running until the user decides to stop
while True:
    print("\n")  # Print a newline for better readability
    x = input("Enter a number: ")  # Get the number from the user
    n = len(x)  # Get the length of the number
    
    # Convert the string to a list of characters for sorting
    digits = list(x)
    
    # Find the largest number by sorting in descending order
    largest_digits = descending(digits.copy(), n)
    largest_number=''.join(largest_digits)  # Join the sorted digits into a string
    print("Largest number : ", largest_number)
    
    # Find the smallest number by sorting in ascending order
    smallest_digits = ascending(digits.copy(), n)
    smallest_number = ''.join(smallest_digits)  # Join the sorted digits into a string
    print("Smallest number : ", smallest_number)
    
    # Ask the user if they want to check another number
    print("\nDo you want to check for another number?")
    iter = input("Enter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break
