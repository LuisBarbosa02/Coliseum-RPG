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
    logger.info(f"{self.name} dealt {attack_damage} of damage to {enemy.type}!")
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
    logger.info(f"{self.type} dealt {attack_damage} of damage to {enemy.name}!")
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


john = Player('John', 'Warrior', 15, {'Cut': [3]})
slime = Monster('Slime', 5, {'Tackle': [1]})