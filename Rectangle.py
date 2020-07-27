# Python Objected-Oriented Programming
import math

class Rectangle:

    def __init__(self,x1,y1,x3,y3):
        self.x1 = x1
        self.y1 = y1

        self.x3 = x3
        self.y3 = y3

        self.x2 = x3
        self.y2 = y1

        self.x4 = x1
        self.y4 = y3

    def test(self):
        print("Suck my dick white America! @Tyler The Creator")

    def area(self):
        return math.fabs(self.y3-self.y1)*math.fabs(self.x1-self.x3)

    def perimetr(self):
        return 2*(math.fabs(self.y3-self.y1)+math.fabs(self.x1-self.x3))

    def print_rectangle(self):
        print("Rectangular consist of:" ,"\n" ,
                "(",self.x1,",",self.y1,")" , '\n' ,
                "(", self.x2,",",self.y2,")" , '\n' ,
                "(", self.x3,",",self.y3,")" , '\n' ,
                "(", self.x4,",",self.y4,")" , '\n')

    def __eq__(self, other):
        EXP = 1E-5
        if not isinstance(other, Rectangle):
            return False
        return (math.fabs(self.x1-other.x1) <=  EXP and math.fabs(self.y1-other.y1) <=  EXP and math.fabs(self.x3-other.x3) <=  EXP and math.fabs(self.y3-other.y3) <=  EXP)

    def common_points(self,other):
        pass

r = Rectangle(0,0,1,1)
other_r = Rectangle(0.5,0.5,2,2)
print(r.x4," ",r.y4)
r.test()
print()
print(r.area())
print(r.perimetr())
r.print_rectangle()
print(r.__eq__(other_r))
print(r.common_points(other_r))
