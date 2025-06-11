class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i{'+' if self.j >= 0 else ''}{self.j}j{'+' if self.k >= 0 else ''}{self.k}k"
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    def __mul__(self,x):
        return self.i*x.i+self.j*x.j+self.k*x.k
    def cross_product(self,x):
        return Vector((self.j*x.k - self.k*x.j),-1*(self.i*x.k - self.k*x.i),(self.i*x.j - self.j*x.i))
    #angle  

    
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
print(v1)
cp = v1.cross_product(v2)
print(cp)


































