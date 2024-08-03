#  DATE : August 3rd,2024
#  MD MAHAFUZUR RAHMAN
#  Roll:2110428176
#  Department of Applied Mathematics
#  University Of Rajshahi.
#  LinkedIn : https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
#  GitHub : https://github.com/itsmahafuz

# Program to chech wheather any given number is prime or not.

def prime(n):
    flag=0
    if(n<1):
        print("Please enter another number.")
    elif(n==1):
        print("The number is not prime.")
    else:
        for i in range(2,n,1):
            if(n%i==0):
                flag=1
        if(flag==1):
            print("The number is not prime.")
        else:
            print("The given number is prime.")
        
while True:
    print("\n")
    n=int(input("Enter a number to check it is prime or not : "))
    
    prime(n)
    print("\n")
    print("Do you want to check for another number?")
    iter=(input("Enter  (y/Y) for Yes and (n/N) for No : "))
    if iter.lower() != 'y':
        break







