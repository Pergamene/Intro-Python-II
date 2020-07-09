from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []

  def get_current_room(self):
    return self.current_room

  def _format_items_for_print(self):
    item_str = ''
    for item in self.items:
      item_str += f'\n    * {item}'
    return item_str if item_str.__len__() else '{none}'

  def get_inventory(self):
    return f'\nInventory: {self._format_items_for_print()}\n'

  def set_current_room(self, current_room):
    self.current_room = current_room

  def take_item(self, item):
    item.on_take()
    self.items.append(item)

  def drop_item(self, name):
    for index, item in enumerate(self.items):
      if item.name == name:
        dropped_item = self.items.pop(index)
        dropped_item.on_drop()
        return dropped_item
    return None
