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

class Monster:
  def __init__(self, type, life, attack_dict):
    self.type = type
    self.life = life
    self.attack_dict = attack_dict
    self.dead = False