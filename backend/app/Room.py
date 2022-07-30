import User
class Room:
  def __init__(self):
    self.users = [],

  def add_user(self, name, id):
    user = User(name, id)
    self.users.append()

  def contains_user(self, name):
    for user in self.users:
        if user.name == name:
            return True
    return False
  
  def get_user_list(self, name):
    ret = []
    for user in self.users:
        ret.append(user.name)
    return ret