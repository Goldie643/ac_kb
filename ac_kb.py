import pygame
from playsound import playsound

pygame.init()

spam = []

sounds_dir = "sounds/"

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            playsound(sounds_dir+event.unicode+".wav")