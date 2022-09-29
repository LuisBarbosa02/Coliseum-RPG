from code_behind import Player, Monster, player_actions, monster_actions

player = Player('John', 'Warrior', 13, {'Punch': [(1, 1)], 'Cut': [(2, 3)], 'Slash': [(3, 5)]})

slime = Monster('Slime', 5, {'Tackle': [(1, 1)], 'Super Tackle': [(2, 3)], 'Body Slam': [(2, 5)]})
snake = Monster('Snake', 7, {'Bite': [(2, 3)], 'Constrict': [(1, 5)], 'Poison': [(2, 2)]})
minotaur = Monster('Minotaur', 19, {'Onslaught': [(4, 8)], 'Punch': [(1, 3)], 'Slash': [(3, 7)]})
monsters = [slime, snake, minotaur]


print(f"\nYou were captured by the romans and now you're a slave. The only way you can survive is to battle day-to-day in a coliseum against all types of monsters. What'll be your fate, {player.name} the {player.type}?\n")
while True:
  monster = monsters.pop(0)
  print(f"\nYou encountered a {monster.type}, prepare for battle!")
  
  while monster.dead is False and player.dead is False:
    player_actions(player, monster)
    if monster.dead:
      break
    monster_actions(monster, player)
  
  if player.dead:
    print(f"\nYou died bravely in combat. Now you can finally rest in peace.")
    break
  
  if not monsters:
    print("\nYou defeat all monsters for today. You'll be able to see tomorrow!")
    break
  
  if monsters:
    print("\nThe day isn't over yet, prepare to battle with more monsters!")