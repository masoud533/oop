class car:
  def __init__(self, carName, carColor):
     self.carName = carName
     self.carColor = carColor

benz = car(carName='A45', carColor='black')

print(benz.carName)