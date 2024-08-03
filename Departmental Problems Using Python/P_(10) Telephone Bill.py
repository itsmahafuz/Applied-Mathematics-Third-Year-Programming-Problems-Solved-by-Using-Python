# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to take input of a user name and minutes spent talking on the
# telephone and print a telephone bill which billing criteria is as follows
# i) First 150 minutes is free of cost
# ii) Next 250 calls (151-400 minute) are charged at the rate of 1
#    TK/minute
# iii) And all calls after 400 minutes, are charged at the rate of
#     2/minute

#Create a function to calculate the telephone bill
def TelephoneBill(min):
    if min<=150 :
        return 0
    elif min<=400 :
        return (min-150)*1
    else :
        return 250+(min-400)*2
        

while True:
    name=input("\nPlease enter your name : ")
    minutes=float(input("\nEnter the minutes spent talking on the telephone : "))
    
    bill=TelephoneBill(minutes)
    print("\n Dear,",name)
    print("Your telephone bill is : ",bill,"Tk.")
    
    # Ask the user if they want to find bill for  another user
    print("\nDo you want to find the telephone bill for another user?")
    iter = input("\nEnter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break