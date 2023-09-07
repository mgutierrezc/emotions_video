from os import environ

SESSION_CONFIGS = [
    dict(
        name='emotions_video',
        display_name="Emotions video",
        num_demo_participants=1,
        app_sequence=['emotions_video_instructions','fer_otree_js','panas_x_initial','emotions_video','panas_x_final']
     ),
     dict(
        name='emotions_video_test',
        display_name="Emotions video test",
        num_demo_participants=3,
        app_sequence=['fer_otree_js']
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
SESSION_CONFIG_DEFAULTS['images_per_second'] = float(environ.get('IMAGES_PER_SECOND', '5'))
SESSION_CONFIG_DEFAULTS['sample_image_frequency'] = int(environ.get('SAMPLE_IMAGE_FREQUENCY', '5'))
SESSION_CONFIG_DEFAULTS['experiment_duration_in_min'] = float(environ.get('EXPERIMENT_DURATION_IN_MIN', '30'))
PARTICIPANT_FIELDS = [

]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='e2labup',
        display_name='E2LabUP',
        participant_label_file='_rooms/e2labup.txt',
        use_secure_urls=False
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'q_qjzz^$_&%)n6m=md!9y24yq%o@i8*^)y06cay9y-vpz+!!tt'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
