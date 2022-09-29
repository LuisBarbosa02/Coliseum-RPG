import logging
import sys
from random import randrange, randint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("{%(levelname)s} - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class Player:
  def __init__(self, name, type, life, attack_dict):
    self.name = name
    self.type = type
    self.life = life
    self.attack_dict = attack_dict
    self.dead = False
  
  def attack(self, attack_name, enemy):
    if attack_name not in self.attack_dict:
      return logger.debug("That attack it's not available!")
    attack_damage = randint(self.attack_dict[attack_name][0][0], self.attack_dict[attack_name][0][1])
    logger.info(f"{self.name}'s {attack_name} dealt {attack_damage} of damage to {enemy.type}.")
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
    logger.info(f"{self.name}'s life: {self.life}")
  
  def die(self):
    self.dead = True
    logger.info(f"{self.name} died!")


class Monster:
  def __init__(self, type, life, attack_dict):
    self.type = type
    self.life = life
    self.attack_dict = attack_dict
    self.dead = False
  
  def attack(self, attack_name, enemy):
    if attack_name not in self.attack_dict:
      return logger.debug("That attack it's not available!")
    attack_damage = randint(self.attack_dict[attack_name][0][0], self.attack_dict[attack_name][0][1])
    logger.info(f"{self.type}'s {attack_name} dealt {attack_damage} of damage to {enemy.name}.")
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
    logger.info(f"{self.type}'s life: {self.life}")
  
  def die(self):
    self.dead = True
    logger.info(f"{self.type} died!")


def player_actions(player, enemy):
  print("\n[ 1: Attack ]")
  choice = int(input("\nThis is what'll do: "))
  if choice == 1:
    attack_string = "\n"
    attack_list = [x for x in player.attack_dict.keys()]
    for i in range(len(player.attack_dict)):
      if i == 0:
        attack_string += f"[ {i+1}: {attack_list[i]} "
      elif i == len(player.attack_dict) - 1:
        attack_string += f" {i+1}: {attack_list[i]} ]"
      else:
        attack_string += f"| {i+1}: {attack_list[i]} |"
    print(attack_string)
    attack_choice = int(input(f"\nI'll attack it with: ")) - 1
    print("")
    player.attack(attack_list[attack_choice], enemy)


def monster_actions(monster, player):
  attack_list = [x for x in monster.attack_dict.keys()]
  monster.attack(attack_list[randrange(len(monster.attack_dict))], player)