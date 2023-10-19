import base64
from io import BytesIO
import os
from random import random
from otree.api import BasePlayer, BaseConstants, BaseGroup, BaseSubsession, models, Page
import requests


# from fer_tools import facial_emotion_recognizer


doc = """
App to get data related to facial expression on every 30 seconds for 200 ms interval.
"""

def variables_dictionary(self):
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

class Constants(BaseConstants):
    timeout1 = 'style_timeout1.html'
    timeout_style = 'timeout_not_auto_submit.html'
    name_in_url = "simulated_emotion"
    image_name_prefix = "image"
    players_per_group = None
    
    contact_template = "fer_otree_js/Contact.html"

    tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num_rounds = len(tasks)


    img_width = 240
    img_height = 180
    img_quality = 90

    # snaps_interval_time_in_sec in (SECONDS)
    #snaps_interval_time_in_sec = get_session_configs()['images_per_second']
    snaps_interval_time_in_sec = 0.2
    
    # sample_image_frequency in (SECONDS)
    sample_image_frequency = 5  # takes 1 sample images for testing purpose each 5 sec

    # experiment_duration_in_sec in (SECONDS)
    experiment_duration_in_sec = 600  # must be in multiple of snaps_interval_time_in_sec

    total_images = int(experiment_duration_in_sec //
                       snaps_interval_time_in_sec)

def creating_session(subsession):
  import random
  if subsession.round_number == 1:
    for p in subsession.get_players():
      round_numbers = list(range(1, Constants.num_rounds+1))
      random.shuffle(round_numbers)
      print(round_numbers)
      p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
      print(p.participant.vars['task_rounds'])


vars = '''
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
'''

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Introduction(Page):
    pass


class FacialCapture(Page):
    form_model = "player"
    # lista = Constants.batches
    # form_fields = lista

    def vars_for_template(self):
        return variables_dictionary(self)

    # @staticmethod
    # def live_method(player, data):
    #     processor_url = "http://localhost:5000/process_live_image"
    #     print(player.participant.__dict__)
    #     print("player.participant.label", player.participant.label)
    #     print(player.__dict__)
    #     requests.post(
    #         processor_url,
    #         json={
    #             "image":"img",# data.get("img"),
    #             "image_name": data.get("img_name"),
    #             "player_id": player.id,
    #             "participate_label": player.participant.label,
    #             "room_name": 'player.participant._session._room_name',
    #             "player_group_id": player.group.id,
    #         },
    #     )
    #     return {0: 0}

class End(Page):
    def vars_for_template(self):
        return variables_dictionary(self)

class VideoCapture(Page):
    pass


class FacialRecognition(Page):
#    def vars_for_template(player):
#        return {
#            
#        }
    def vars_for_template(self):
        return variables_dictionary(self)

class Page1_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['A']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page1_b(Page):
    timeout_seconds = 15
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['A']
    def vars_for_template(self):
        return variables_dictionary(self)
    
class Page2_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['B']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page2_b(Page):
    timeout_seconds = 15
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['B']
    def vars_for_template(self):
        return variables_dictionary(self)
    
class Page3_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['C']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page3_b(Page):
    timeout_seconds = 20
    def vars_for_template(self):
        return variables_dictionary(self)
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['C']

class Page4_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['D']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page4_b(Page):
    timeout_seconds = 20
    def vars_for_template(self):
        return variables_dictionary(self)
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['D']
    
class Page5_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['E']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page5_b(Page):
    timeout_seconds = 20
    def vars_for_template(self):
        return variables_dictionary(self)
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['E']
    
class Page6_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['F']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page6_b(Page):
    timeout_seconds = 20
    def vars_for_template(self):
        return variables_dictionary(self)
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['F']
    
class Page7_a(Page):
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['G']
    def vars_for_template(self):
        return variables_dictionary(self)
class Page7_b(Page):
    timeout_seconds = 20
    def vars_for_template(self):
        return variables_dictionary(self)
    def is_displayed(player):
        return player.round_number == player.participant.vars['task_rounds']['G']


#page_sequence_initial = [Introduction, Page1_a,Page1_b, Page2_a, Page2_b, Page3, Page4, Page5, Page6, Page7]
#random.shuffle(page_sequence_initial)

page_sequence = [Page1_a, Page2_a, Page3_a, Page4_a, Page5_a, Page6_a, Page7_a, Page1_b, Page2_b, Page3_b, Page4_b, Page5_b, Page6_b, Page7_b]
