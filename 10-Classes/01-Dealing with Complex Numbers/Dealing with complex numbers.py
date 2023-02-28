#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=true

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex((self.real*no.real)-(self.imaginary*no.imaginary),(self.imaginary*no.real)+(self.real*no.imaginary))
    def __truediv__(self, no):
        x= complex(self.real,self.imaginary)
        y=complex(no.real,no.imaginary)
        z=x/y
        return Complex(z.real,z.imag)
    def mod(self):
        x= complex(self.real,self.imaginary)
        return Complex(abs(x),0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

