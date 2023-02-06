class User:
  UserActiveCount = 0
  alloweduser = ['masoud', 'mohammad',  'sara']
  loggedInUsers = []
  def __init__(self, userName, userFamily):
      if userName  not in User.alloweduser:
        raise ValueError(f'{userName} can not login !!')
      self.name = userName
      self.family = userFamily
      User.UserActiveCount += 1
      User.loggedInUsers.append(self.name)
      print(f'User {self.name} has logged in')
      print(f'active user: {User.UserActiveCount}')
  def logOut(self):
    User.UserActiveCount -= 1
    print(f'User {self.name} has logged out')
    print(f'active user: {User.UserActiveCount}')
    User.loggedInUsers.remove(self.name)

masoud = User('masoud', 'mapar')
mohammad = User('mohammad', 'mapar')
masoud.logOut()
mohammad.logOut()

