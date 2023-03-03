from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Video1(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.first_ROLE
class Video2(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.second_ROLE

class Video3(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.third_ROLE


page_sequence = [Video1, Video2, Video3]
