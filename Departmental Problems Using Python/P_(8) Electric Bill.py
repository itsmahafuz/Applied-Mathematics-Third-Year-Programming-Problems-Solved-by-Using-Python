# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to take input of a user name and consumed current units and print
# an electric bill which billing criteria is as follows
# i) First 50 units has minimum charge 100tk
# ii) Next 200 units cost 2.50 TK/unit
# iii) Next 250 units cost 3.50 TK/unit
# iv) Units above 500 are charged at a rate 5.00TK/unit
# Make sure you implement the idea using user-defined function.

#Create a function to claculate the electric bill
def ElectricBill(ut):
    if(ut<=50):
        taka=100
    elif(ut>50 and ut<=250):
        taka=100+(ut-50)*2.50
    elif(ut>250 and ut<=500):
        taka=100+200*2.50+(ut-250)*3.50
    else:
        taka=100+200*2.50+250*3.50+(ut-500)*5.00
    return taka

while True:
    name=input("\nPlease Enter user name : ")
    units=float(input("Enter the amount of consumed current units : "))
    
    #Call the Electric Bill function to get electric bill
    bill=ElectricBill(units)
    print("\n Dear,",name)
    print("Your electric bill is : ",bill," Tk.")
    
    
    # Ask the user if they want to find bill for  another user
    print("\nDo you want to find  the electric  for another user?")
    iter = input("Enter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break
    