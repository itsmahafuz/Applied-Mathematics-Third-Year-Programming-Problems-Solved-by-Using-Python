# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to sort a list of numbers in ascending and descending order (Without using built-in functions).

# Function to sort a list of numbers in ascending order
def ascending(list, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            # Swap if the element found is greater than the next element
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

# Function to sort a list of numbers in descending order
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
    n = int(input("Enter the number of elements: "))  # Get the number of elements from the user
    li = []  # Initialize an empty list to store the elements
    
    # Get the elements from the user
    print("Enter the elements column-wise: ")
    for i in range(0, n):
        li.append(int(input()))  # Append each entered element to the list
    
    # Print the original list
    print("\nOriginal list: ", li)
    
    # Now call the function for ascending order
    ascending_order = ascending(li.copy(), n)  # Use .copy() to avoid modifying the original list
    print("The ascending order is: ", ascending_order)
    
    # Now call the function for descending order
    descending_order = descending(li.copy(), n)  # Use .copy() to avoid modifying the original list
    print("The descending order is: ", descending_order)
    
    # Ask the user if they want to check another list
    print("\nDo you want to check for another list?")
    iter = input("Enter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break

