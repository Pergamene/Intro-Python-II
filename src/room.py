from item import Item

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.items = []

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

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, name):
    for index, item in enumerate(self.items):
      if item.get_name() == name:
        return self.items.pop(index)
    return None

  def _format_items_for_print(self):
    item_str = ''
    for item in self.items:
      item_str += f'\n    * {item}'
    return item_str if item_str.__len__() else '{none}'

  def __str__(self): 
    return f'\n{self.name} -\n  {self.description}\n  Items: {self._format_items_for_print()}\n'
