import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("{%(levelname)s}\n%(message)s")
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
    if attack_name not in attack_dict:
      return logger.debug("That attack it's not available!")
    attack_damage = self.attack_dict[attack_name][0]
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
  
  def die(self):
    self.dead = True

class Monster:
  def __init__(self, type, life, attack_dict):
    self.type = type
    self.life = life
    self.attack_dict = attack_dict
    self.dead = False
  
  def attack(self, attack_name, enemy):
    if attack_name not in attack_dict:
      return logger.debug("That attack it's not available!")
    attack_damage = self.attack_dict[attack_name][0]
    enemy.lose_hp(attack_damage)

  def lose_hp(self, attacker_damage):
    self.life -= attacker_damage
    if self.life <= 0:
      self.life = 0
      return self.die()
  
  def die(self):
    self.dead = True