class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def get_name(self):
    return self.name

  def on_take(self):
    print(f'\nYou have picked up {self.name}')

  def on_drop(self):
    print(f'\nYou have dropped {self.name}')

  def __str__(self):
    return f'{self.name} -\n        {self.description}'
