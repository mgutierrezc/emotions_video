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


doc = """
Panas-x-scale
"""


class Constants(BaseConstants):
    name_in_url = 'panas_x_final'
    players_per_group = None
    num_rounds = 1
    panasx_list=[
        'Animado/a',
        'Repugnado/a',
        'Atento/a',
        'Vergonzoso/a',
        'Lento/a',
        'Atrevido/a',
        'Sorprendido/a',
        'Fuerte',
        'Desdeñoso/a',
        'Relajado/a',
        'Irritable',
        'Encantado/a',
        'Inspirado/a',
        'Sin miedo',
        'Disgustado con uno mismo',
        'Triste',
        'Calmado/a',
        'Temeroso/a',
        'Cansado/a',
        'Atónito/a',
        'Tembloroso/a',
        'Feliz',
        'Tímido/a',
        'Solo/a',
        'Alerta',
        'Decepcionado/a',
        'Enojado/a',
        'Audaz',
        'Melancólico/a',
        'Retraído/a',
        'Activo/a',
        'Culpable',
        'Jubiloso/a',
        'Nervioso/a',
        'Solitario/a',
        'Somnoliento/a',
        'Emocionado/a',
        'Hostil',
        'Orgulloso/a',
        'Inquieto/a',
        'Lleno de vida',
        'Avergonzado/a',
        'Cómodo/a',
        'Asustado/a'
        'Adormecido/a'
        'Enojado con uno mismo',
        'Entusiasmado',
        'Decaído/a',
        'Inseguro/a',
        'Afligido/a',
        'Reprensible',
        'Determinado/a',
        'Atemorizado/a',
        'Estupefacto/a',
        'Interesado/a',
        'Averso/a',
        'Seguro/a',
        'Energético/a',
        'Concentrado/a',
        'Insatisfecho con uno mismo'
    ]
    list_size = len(panasx_list)
    num_emo_pg1 = int(round(list_size / 2, 0))
    num_emo_pg2 = list_size - num_emo_pg1


class Subsession(BaseSubsession):
    def creating_session(subsession):
        panasx_list = random.sample(Constants.panasx_list, len(Constants.panasx_list))
        subsession.session.vars['panasx_list_1'] = panasx_list[:Constants.num_emo_pg1]
        subsession.session.vars['panasx_list_2'] = panasx_list[Constants.num_emo_pg1:]
    


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    for var_name in Constants.panasx_list:
        locals()[var_name] = models.IntegerField(
                                                    initial = None,
                                                    choices = [[num, str(num)] for num in range(1, 6)],
                                                    label = var_name,
                                                    widget = widgets.RadioSelectHorizontal()
                                                )

    del var_name

    Q1 = models.StringField(
        choices = [
        'Flores en un jardin',
        'Personas practicando un deporte extremo en un cañón',
        'Buceando y surfeando con las tortugas',
        'Personas caminando en una avenida',
        'Un salón de clase lleno'
        ],
        label = '1. ¿Cuál es el tema principal del video? (se califica)'
    )
    Q2 = models.LongStringField(
        label = '2. Describe brevemente algún evento que sucede durante el video (no se califica)'
    )

