import math

''' Implementation with functions '''
PI = 3.14159
E = 2.71828

def circle_area(radius):
    return PI * math.pow(radius, 2)

def circle_circumf(radius):
    return PI * radius * 2

def exp(power):
    return math.pow(E, power)

#... other code, bla bla bla ...

E = "echo"
#print(exp(2))

# Redefinition breaks code!!

''' Implementation with classes '''

class Calculator(object):
    ''' Wrapper for mathematical operations '''
    def __init__(self):
        self.pi = 3.14159
        self.e = 2.71828
    
    def circle_area(self, radius):
        return self.pi * math.pow(radius, 2)
    
    def circle_circumf(self, radius):
        return self.pi * 2 * radius
    
    def exp(self, x):
        return math.pow(self.e, x)


calc = Calculator() # Make an instance of class

e = "echo"
print(calc.exp(2))

print("~~ SUCCESS! ~~")