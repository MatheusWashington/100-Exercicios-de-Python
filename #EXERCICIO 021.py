# Faça um programa em Python que abra e reproduza um arquivo mp3
import time

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)


