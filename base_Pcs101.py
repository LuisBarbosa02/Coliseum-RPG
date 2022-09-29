from code_behind import Player, Monster, player_actions, monster_actions

player = Player('John', 'Warrior', 15, {'Punch': [(1, 1)], 'Cut': [(2, 3)], 'Slash': [(3, 5)]})

slime = Monster('Slime', 5, {'Tackle': [(1, 1)], 'Super Tackle': [(2, 3)], 'Body Slam': [(2, 5)]})
monsters = [slime]


print(f"\nYou were captured by the romans and now you're a slave. The only way you can survive is to battle day-to-day in a coliseum against all types of monsters. What'll be your fate, {player.name} the {player.type}?\n")
while player.dead is False and len(monsters) > 0:
  monster = monsters.pop(0)
  print(f"\nYou encountered a {monster.type}, prepare for battle!")
  
  while monster.dead is False and player.dead is False:
    player_actions(player, monster)
    if monster.dead:
      break
    monster_actions(monster, player)