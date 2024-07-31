#30-07-2024

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def DistanceFromOrigin(self): #calculates point distance from (0,0)
        return(self.x**2+self.y**2)**0.5
    def DistanceFromPoint(self,other): #calculates distance from point to point
        return((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def retPoint(self): #returns point cordinations into a tuple
        return (self.x, self.y)
    def __repr__(self): #works for strings only
        return str((self.x,self.y))


p1 = Point(1,2)
p2 = Point(2,3)

# print(p1.x,p1.y) #manually printing an object
# print(p2.x,p2.y)
# print(p1.DistanceFromOrigin()) #refers to line 5
# print(p1.DistanceFromPoint(p2)) #refers to line 7
# print(p1) #refers to line 11
# print(p1.retPoint()) #refers to line 9

class Circle:
    def __init__(self,radius,point):
        self.radius = radius
        self.point = point
    def area(self):
        return 3.14*self.radius**2
    def heikef(self):
        return 2*3.14*self.radius
    def koter(self):
        return self.radius*2
    def __repr__(self):
        return str(self.radius)+", "+str(self.point)
    def DistanceFromAnotherCircle(self, other):
        return self.point.DistanceFromPoint(other.point)
    def TouchCheck(self, other):
        RadiusSum = self.radius + other.radius
        if self.point.DistanceFromPoint(other.point) > RadiusSum:
                return False
        return True

p1 = Point(2,4)
p2 = Point(2,4)

c1 = Circle(8, p1)
c2 = Circle(2, p2)

print(c1.TouchCheck(c2))