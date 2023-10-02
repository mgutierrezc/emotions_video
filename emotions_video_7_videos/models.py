import os
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
    name_in_url = 'emotions_video_7_videos'
    players_per_group = 3
    num_rounds = 1
    roles = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    first_ROLE = roles[0]
    second_ROLE = roles[1]
    third_ROLE = roles[2]
    fourth_ROLE = roles[3]
    fifth_ROLE = roles[4]
    sixth_ROLE = roles[5]
    seventh_ROLE = roles[6]

    Contactenos = 'emotions_video/Contactenos.html'

    image_name_prefix = "image"
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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

