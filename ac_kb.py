import pygame
from playsound import playsound
import string

pygame.init()

spam = []

sounds_dir = "sounds/"

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode in string.ascii_lowercase:
                playsound(sounds_dir+event.unicode+".wav",False)