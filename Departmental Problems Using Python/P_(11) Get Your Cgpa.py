# DATE : August 3rd, 2024
# MD MAHAFUZUR RAHMAN
# Roll: 2110428176
# Department of Applied Mathematics
# University Of Rajshahi.
# LinkedIn: https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
# GitHub: https://github.com/itsmahafuz

# Program to take input of the name  of a third year student of Applied
# Mathematics, RU and marks obtained in all courses including LAB and
# viva, and print the overall GPA in year three following the standard grading
# criteria of Applied Mathematics.

# In the third year, there are 11 courses including LAB and Viva.
# Where full mark of Viva course is 50 and full mark of the others are 100.

# Function to determine the grade point based on the marks
def grade(mk):
    if mk >= 80:
        return 4.00
    elif mk >= 75:
        return 3.75
    elif mk >= 70:
        return 3.50
    elif mk >= 65:
        return 3.25
    elif mk >= 60:
        return 3.00
    elif mk >= 55:
        return 2.75
    elif mk >= 50:
        return 2.50
    elif mk >= 45:
        return 2.25
    elif mk >= 40:
        return 2.00
    else:
        return 0.00

# Function to calculate the sum of credit * grade points
def SumOFCreditGrade(g):
    return sum(g)

while True:
    name = input("\nPlease enter your name: ")
    roll = int(input("\nEnter your roll no.: "))
    
    marks = [] # List to store marks
    cgd = []   # List to store credit * grade points
    
    # Input marks for 9 main courses
    for i in range(9):
        mark = int(input(f"\nEnter marks (0-100) obtained in the course A.Math-30{i+1}: "))
        marks.append(mark)
        cgd.append(grade(mark) * 4)
    
    # Input marks for Lab course A.Math-320
    lab_mark = int(input("\nEnter marks (0-100) obtained in the course A.Math-320: "))
    marks.append(lab_mark)
    cgd.append(grade(lab_mark) * 4)
    
    # Input marks for Viva course A.Math-321 (full mark is 50)
    viva_mark = int(input("\nEnter marks (0-100) obtained in the course A.Math-321: "))
    marks.append(viva_mark * 2)  # Scale viva marks to 100
    cgd.append(grade(viva_mark * 2) * 4)
    
    # Check if the student failed in Lab or Viva
    if lab_mark < 40 or viva_mark < 40:
        print("\nYour CGPA is: 0.00")
        print("\nSorry! You fail.\n")
    else:
        # Check if the student failed more than 2 courses
        fail_count = sum(1 for mark in marks if mark < 40)
        if fail_count > 2:
            print("\nYour CGPA is: 0.00")
            print("\nSorry! You fail.\n")
        else:
            # Calculate and print CGPA
            cgpa = SumOFCreditGrade(cgd) / 44  # Total credit = 11 * 4 = 44
            formatted_cgpa = format(cgpa, ".3f") #This will help to print upto three decimal place
            print("\nYour CGPA is : ",formatted_cgpa)
            print("\nCongratulations! You pass.\n")
    
   
    # Ask if the user wants to calculate CGPA for another student
    iter = input("\nDo you want to find the CGPA for another student? Enter (y/Y) for Yes and (n/N) for No: ")
    if iter.lower() != 'y':
        break
