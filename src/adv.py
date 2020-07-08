import textwrap
from room import Room
from player import Player

# Declare all the rooms
room = {
  'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
  'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),
  'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
  'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),
  'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def input_parser(input):
  inputArr = input.split(' ')
  first = inputArr[0]
  second = inputArr[1] if inputArr.__len__() > 1 else ''
  if second == '':
    if first == 'q':
      return True
    elif first == 'n':
      next_room = player.get_current_room().get_n_to()
      if next_room is not None:
        player.set_current_room(next_room)
      else:
        print('\nThere is no room to the North')
    elif first == 's':
      next_room = player.get_current_room().get_s_to()
      if next_room is not None:
        player.set_current_room(next_room)
      else:
        print('\nThere is no room to the South')
    elif first == 'e':
      next_room = player.get_current_room().get_e_to()
      if next_room is not None:
        player.set_current_room(next_room)
      else:
        print('\nThere is no room to the East')
    elif first == 'w':
      next_room = player.get_current_room().get_w_to()
      if next_room is not None:
        player.set_current_room(next_room)
      else:
        print('\nThere is no room to the West')
    elif first == 'i' or first == 'inventory':
      print(f'\n{player.get_inventory()}')
    else:
      print('\nPlease enter a valid command (n, s, e, w) or (q)')
  else:
    if first == 'get' or first == 'take':
      item = player.get_current_room().remove_item(second)
      if item is not None:
        player.take_item(item)
      else:
        print(f'\nThis room does not have the item: {second}')
    elif first == 'drop':
      item = player.drop_item(second)
      if item is not None:  
        player.get_current_room().add_item(item)
      else:
        print(f'\nYou do not have the item: {second}')
  return False

def start_game():
  # Write a loop that:
  # * Prints the current room name
  # * Prints the current description (the textwrap module might be useful here).
  # * Waits for user input and decides what to do.
  #
  # If the user enters a cardinal direction, attempt to move to the room there.
  # Print an error message if the movement isn't allowed.
  #
  # If the user enters "q", quit the game.
  end_game = False
  while not end_game:
    print(player.current_room)
    player_input = input(f'\tPlease pick an available direction (n, s, e, w),\n\tpick up items (get [item], take [item]),\n\tdrop items (drop [item]),\n\tview inventory(i, inventory),\n\tor quit (q): ')
    end_game = input_parser(player_input.lower())

# Make a new player object that is currently in the 'outside' room.
player = Player('Bast', room['outside'])

start_game()
