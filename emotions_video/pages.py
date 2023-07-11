from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os

def diccionario(self):
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
class Video1(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.first_ROLE
    def vars_for_template(self):
        return diccionario(self)

class Video2(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.second_ROLE
    def vars_for_template(self):
        return diccionario(self)

class Video3(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.role == Constants.third_ROLE
    def vars_for_template(self):
        return diccionario(self)


page_sequence = [Video1, Video2, Video3]
