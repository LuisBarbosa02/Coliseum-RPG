import logging
import sys

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
    attack_damage = self.attack_dict[attack_name][0]
    logger.info(f"{self.name}'s {attack_name} dealt {attack_damage} of damage to {enemy.type}.")
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
    logger.info(f"{self.name} life: {self.life}")
  
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
    attack_damage = self.attack_dict[attack_name][0]
    logger.info(f"{self.type}'s {attack_name} dealt {attack_damage} of damage to {enemy.name}.")
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
    logger.info(f"{self.type} life: {self.life}")
  
  def die(self):
    self.dead = True
    logger.info(f"{self.type} died!")


def player_actions(player, enemy):
  print("\n1 - Attack")
  choice = int(input("\nWhat'll you do? "))
  if choice == 1:
    attack_string = "\n"
    attack_list = [x for x in player.attack_dict.keys()]
    for i in range(len(player.attack_dict)):
      attack_string += f"{i+1} - {attack_list[i]} | "
    print(attack_string)
    attack_choice = int(input(f"\nWhat attack will you choose? ")) - 1
    print("")
    player.attack(attack_list[attack_choice], enemy)