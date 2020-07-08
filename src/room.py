# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to: None
    self.s_to: None
    self.e_to: None
    self.w_to: None

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description
    
  def get_n_to(self):
    return self.n_to

  def get_s_to(self):
    return self.s_to

  def get_e_to(self):
    return self.e_to
    
  def get_w_to(self):
    return self.w_to

  # Rooms able to hold multiple items
