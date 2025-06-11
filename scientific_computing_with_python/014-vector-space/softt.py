class R2Vector:
    def __init__(self,*,x,y):
        self.x=x
        self.y=y
    def norm(self):
        return sum(val**2 for val in self.__dict__.values())**0.5
class R3Vector(R2Vector):
    def __init__(self,*,x,y,z):
        super().__init__(x=x,y=y)
        self.z=z 
        
v1= R2Vector(x=1,y=2)
print(v1.__dict__.values())