import math

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    #decides how thr obj is printed as string
    def __str__(self):
        return f"{self.i}i{'+' if self.j >= 0 else ''}{self.j}j{'+' if self.k >= 0 else ''}{self.k}k"
    #addition
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    #substraction
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    #dot product
    def __mul__(self,x):
        return self.i*x.i+self.j*x.j+self.k*x.k
    #cross product 3d
    def cross_product(self,x):
        return Vector((self.j*x.k - self.k*x.j),-1*(self.i*x.k - self.k*x.i),(self.i*x.j - self.j*x.i))
    #magnitude
    def __abs__(self):
        return round(math.sqrt((self.i)**2+(self.j)**2+(self.k)**2),3)
    def magnitude(self):
        return math.sqrt((self.i)**2+(self.j)**2+(self.k)**2)
    #agle
    def angle_with(self,x):
        magnitude_1=abs(self)
        magnitude_2=abs(x)

        if magnitude_1==0 or magnitude_2==0:
            raise ValueError("Cannot find angle with 0 vector")
        else:
            cos = (self*x)/(magnitude_1*magnitude_2)
            rad = math.acos(cos)
            deg = math.degrees(rad)
            return deg

































