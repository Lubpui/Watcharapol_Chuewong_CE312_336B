class Pyramid():
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

class Calculate():
    def CalResult(self,l,w,h):
        py = Pyramid(l,w,h)
        self.Result = (py.length*py.width*py.height)/3
        return self.Result

PyCal = Calculate()
print("volume of pyramid  = ",PyCal.CalResult(10,7,17))


