class Cylinder():
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def Calculate(self):
        self.Result = 3.14*(self.Radius*self.Radius)*self.Height
        return self.Result

Fcylin = Cylinder(5,10)
Scylin = Cylinder(7,13)

print("--------First Cylinder--------")
print("Radius : ", Fcylin.Radius)
print("Height : ", Fcylin.Height)
print("Result : ", Fcylin.Calculate())
print("-------Second Cylinder-------")
print("Radius : ", Scylin.Radius)
print("Height : ", Scylin.Height)
print("Result : ", Scylin.Calculate())
print("---------------------------")

