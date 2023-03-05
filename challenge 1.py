class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def sqsum(self):
        return (f'The sum is {self.x**2+self.y**2+self.z**2}')

#object 

a=point(1,3,5)
print(a.sqsum())
     

