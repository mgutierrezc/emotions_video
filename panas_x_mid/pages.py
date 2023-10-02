from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os


# diccionario para face capture
def face_capture(self):
    return {
    "result": self.participant.vars.get("result", None),
    "image_name_prefix": Constants.image_name_prefix,
    "snaps_interval_time_in_sec": float(1 / self.session.config['images_per_second']),
    "experiment_duration_in_sec": float(self.session.config['experiment_duration_in_min'] * 60),
    "participant_id": self.participant.id,
    "img_width": Constants.img_width,
    "img_height": Constants.img_height,
    "img_quality": Constants.img_quality,
    "sample_image_frequency": Constants.sample_image_frequency,
    "processor_endpoint_sample": os.environ.get("FER_PROCESS_URL", "https://faceprocessing.tech/process_live_image"),
    "processor_endpoint_all": os.environ.get("FER_PROCESS_URL_ALL", "https://faceprocessing.tech/process_all_images"),
    "api_key": os.environ.get("PROCESSING_APP_API_KEY", 'xadsaid9s0aS*SDIHSDS%')
}


class EmoQuestPage1(Page):
    form_model = 'player'
    def get_form_fields(player):
        lista = ['{}'.format(var) for var in player.session.vars['panasx_list_1']]
        #fields = ['{}'.format(var) for var in player.session.vars['panasmauss_list_1']]
        #fields.append('time_EmoQuestPage1')
        return lista

    #def vars_for_template(player):
        #return {
        #    'emotions': player.session.vars['panasx_list_1'],
        #}
    def vars_for_template(self):
        dictionary = {
            'emotions': self.player.session.vars['panasx_list_1'],
        }
        
        player_vars = face_capture(self)
        dictionary.update(player_vars)
        
        return dictionary    

class EmoQuestPage2(Page):
    form_model = "player"

    def get_form_fields(player):
        lista = ['{}'.format(var) for var in player.session.vars['panasx_list_2']]
        return lista

    #def vars_for_template(player):
    #    return {
    #        'emotions': player.session.vars['panasx_list_2']
    #    }    
    def vars_for_template(self):
        dictionary = {
            'emotions': self.player.session.vars['panasx_list_2']
        }
        
        player_vars = face_capture(self)
        dictionary.update(player_vars)
        
        return dictionary

class DoneQuestionnaire(Page):
    def vars_for_template(self):
        return face_capture(self)

page_sequence = [EmoQuestPage1, EmoQuestPage2, DoneQuestionnaire]

