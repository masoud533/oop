class User:

  def __init__(self, name, family, age):
    self.name = name
    self.family = family
    self.age = age

  def __repr__(self):
    return f'{self.name} {self.family} \n {self.age} years old'


me = User('masoud', 'mapar', 18)

print(me.name)
print(me.family)
print(me.age)
print(me)