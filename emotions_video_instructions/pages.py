from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants 

class E2LabUP_initial(Page):
    pass

class InstructionsFer(Page):
    pass

class Instructions(Page):
    pass

page_sequence = [E2LabUP_initial, InstructionsFer, Instructions]

