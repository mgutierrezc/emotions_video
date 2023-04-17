from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'emotions_video'
    players_per_group = None
    num_rounds = 1
    first_ROLE = 'A'
    second_ROLE = 'B'
    third_ROLE = 'C'
    Contactenos = 'emotions_video/Contactenos.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

