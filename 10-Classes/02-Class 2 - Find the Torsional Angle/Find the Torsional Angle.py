#https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true


class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __sub__(self, no):
        ans=[]
        a=[self.x,self.y,self.z]
        b=[no.x,no.y,no.z]
        for i in range(3):
            ans.append(a[i]-b[i])
        return Points(ans[0],ans[1],ans[2])
    def dot(self, no):
        return self.x*no.x+self.y*no.y+self.z*no.z
        
    def cross(self, no):
        Cro = [(self.y*no.z)-(self.z*no.y), (self.z*no.x)-(self.x*no.z), (self.x*no.y)-(self.y*no.x)]
        return Points(Cro[0],Cro[1],Cro[2])
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)