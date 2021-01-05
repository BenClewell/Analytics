from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pygame.mixer.pre_init(
    frequency=44100, size=-16, channels=2, buffer=512, devicename=None
)
pygame.mixer.init()

yes_viz = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/disable.wav")
no_viz = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/enable.wav")
click = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/confirmation2.wav"
)
launch = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/launch.wav")
boring_click = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/click.wav"
)
propagate_info = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/propagate2.wav"
)
gen_1 = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/gen_1.wav")
gen_2 = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/gen_2.wav")
gen_3 = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/gen_3.wav")
gen_4 = pygame.mixer.Sound("Resources/effects_and_calcs/sounds/gen_4.wav")
bass = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/-48 semitones_fast.wav"
)


# effects for generating graphs

graph_sfx_1 = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/graph_generation_sounds/PM_CSPH_Terminal_1.ogg"
)
graph_sfx_2 = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/graph_generation_sounds/PM_CSPH_Terminal_2.ogg"
)
graph_sfx_3 = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/graph_generation_sounds/PM_CSPH_Terminal_3.ogg"
)
graph_sfx_4 = pygame.mixer.Sound(
    "Resources/effects_and_calcs/sounds/graph_generation_sounds/PM_CSPH_Terminal_4.ogg"
)

graph_sound_list = [graph_sfx_1, graph_sfx_2, graph_sfx_3, graph_sfx_4]