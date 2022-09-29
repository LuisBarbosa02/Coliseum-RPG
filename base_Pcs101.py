from code_behind import Player, Monster, player_actions

player = Player('John', 'Warrior', 15, {'Cut': [3], 'Slash': [5]})

slime = Monster('Slime', 5, {'Tackle': [1]})
monsters = [slime]


while player.dead is False and len(monsters) > 0:
  monster = monsters.pop(0)
  player_actions(player, monster)