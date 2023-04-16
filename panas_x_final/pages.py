from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class EmoQuestPage1(Page):
    form_model = 'player'
    def get_form_fields(player):
        lista = ['{}'.format(var) for var in player.session.vars['panasx_list_1']]
        #fields = ['{}'.format(var) for var in player.session.vars['panasmauss_list_1']]
        #fields.append('time_EmoQuestPage1')
        return lista

    def vars_for_template(player):
        return {
            'emotions': player.session.vars['panasx_list_1'],
        }    

class EmoQuestPage2(Page):
    form_model = "player"

    def get_form_fields(player):
        lista = ['{}'.format(var) for var in player.session.vars['panasx_list_2']]
        return lista

    def vars_for_template(player):
        return {
            'emotions': player.session.vars['panasx_list_2']
        }    

class DoneQuestionnaire(Page):
    pass

class Final_E2lab(Page):
    def vars_for_template(self):
        return dict(participant_id=self.participant.label)



page_sequence = [EmoQuestPage1, EmoQuestPage2, DoneQuestionnaire, Final_E2lab]

