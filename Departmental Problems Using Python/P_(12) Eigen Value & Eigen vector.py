#  DATE : August 9,2024
#  MD MAHAFUZUR RAHMAN
#  Roll:2110428176
#  Department of Applied Mathematics,
#  University Of Rajshahi.
#  LinkedIn : https://www.linkedin.com/in/md-mahafuzur-rahman-07b80b1b7
#  GitHub : https://github.com/itsmahafuz

# Program to find the dominant eigenvalue and corresponding eigenvector of
# a given non-diagonal square matrix.

class EigenValueAndVector:
    
    def __init__(self, size, accuracy):
        self.accuracy = accuracy
        self.n = size
        self.matrix = []  # Initialize the 2D array for the matrix
        self.InG = []  # Initialize the array for the initial guess
        self.c = [0] * self.n  # Initialize the array to store intermediate results
    
    def GetMatrix(self):
        print("\nEnter the elements of the matrix (row-wise):\n")
        for i in range(self.n):  # A loop for row entries
            a = []
            for j in range(self.n):  # A loop for column entries
                element = int(input(f"Element [{i+1},{j+1}]: "))
                a.append(element)
            self.matrix.append(a)
    
    def GetInitialGuess(self):
        print("\nEnter the initial guess for the eigenvector:\n")
        for i in range(self.n):
            element = float(input(f"Element [{i+1},1]: "))
            self.InG.append(element)
    
    def CalculateEigen(self):
        k = self.InG[0]  # Assign some initial value to eigenvalue
        y = 0
        
        while abs(k - y) >= self.accuracy:
            y = k
            for i in range(self.n):
                self.c[i] = 0
                for j in range(self.n):
                    self.c[i] += self.matrix[i][j] * self.InG[j]
            k = abs(self.c[0])
            for i in range(1, self.n):
                if k < abs(self.c[i]):
                    k = abs(self.c[i])
            # Calculate the eigenvector
            for i in range(self.n):
                self.InG[i] = self.c[i] / k
        
        print(f"\nThe largest eigenvalue is: {k:.3f}")
        print("\nAnd the corresponding eigenvector is: ")
        for i in range(self.n):
            print(f"{self.InG[i]:.3f}")
    



while True:
    n=int(input("\nEnter the order of the square matrix: "))
    eps=float(input("\nEnter the desired accuracy: "))
    E=EigenValueAndVector(n,eps)
    E.GetMatrix()
    E.GetInitialGuess()
    E.CalculateEigen()
    
    print("\nDo you want to find eigenvector and eigenvalue for another matrix?")
    choose=input("\nFor yes then press y/Y and for no press N/n : ")
    if choose.lower()!='y':
        break