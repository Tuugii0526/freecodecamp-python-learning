class R2Vector:
    def __init__(self,*,x,y):
        self.x=x
        self.y=y
    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5
    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))
    def __repr__(self):
        arg_list=[f'{key}={value}' for key,value in vars(self).items()]
        args=', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'
    def __add__(self,other):
        if type(self)!= type(other):
            return NotImplemented
        kwargs= { i: getattr(self, i)+getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    def __sub__(self,other):
        if type(self)!=type(other):
            return NotImplemented
        kwargs= { i: getattr(self, i)-getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    def __mul__(self,other):
        if type(other) in (float ,int):
            kwargs= {i:getattr(self, i)*other for i in vars(self)}
        elif type(other) ==type(self):
            return sum(getattr(self, i)*getattr(other, i) for i in vars(self))
    def __eq__(self , other):
        if type(self)!= type(other):
            return NotImplemented
        return all(getattr(self,i)== getattr(other,i) for i in vars(self))
    def __ne__(self , other):
        return not self == other 
    def __lt__(self,other):
        if type(self)!= type(other):
            return NotImplemented
        return self.norm() < other.norm()
    def __gt__(self,other):
        if type(self)!= type(other):
            return NotImplemented
        return self.norm() > other.norm()
    def __ge__(self,other):
        return not self < other 
    def __le__(self,other):
        return not self > other 
            
class R3Vector(R2Vector):
    def __init__(self,*,x,y,z):
        super().__init__(x=x,y=y)
        self.z=z 
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)
v1= R2Vector(x=1,y=2)
