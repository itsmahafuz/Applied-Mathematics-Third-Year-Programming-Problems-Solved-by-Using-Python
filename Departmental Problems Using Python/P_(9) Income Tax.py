# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to take input of a user name and yearly income and print income
# tax where the taxation criteria is as follows
# i) First 250000 is tax free
# ii) 5% tax for next 250000
# iii) 10% tax for next 500000
# iv) 20% tax for next 4000000
# v) 40% tax for income above 5000000 

#Create a function to calculate the income tax
def IncomeTax(yi):
    if yi <= 250000:
        return 0
    elif yi <= 500000:
        return (yi - 250000) * 0.05
    elif yi <= 1000000:
        return 250000 * 0.05 + (yi - 500000) * 0.1
    elif yi <= 5000000:
        return 250000 * 0.05 + 500000 * 0.1 + (yi - 1000000) * 0.2
    else:
        return 250000 * 0.05 + 500000 * 0.1 + 4000000 * 0.2 + (yi - 5000000) * 0.4
    

while True:
    name=input("\nPlease Enter user name : ")
    income=float(input("Enter the amount of your yearly income : "))
    
    #Call the Income tax function
    tax=IncomeTax(income)
    
    print("\n Dear,",name)
    print("Your income tax is : ",tax," Tk.")
    
    
    # Ask the user if they want to find bill for  another user
    print("\nDo you want to find  the electric bill for another user?")
    iter = input("Enter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break