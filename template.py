from pynput.mouse import Listener
import logging
import pygame
import time
import random
import os
import sys

CHANCE      = 0.20
AUDIO_FILE  = "audio.mp3"
VOLUME      = 0.05

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)

    return os.path.join(os.path.abspath("."), filename)

pygame.mixer.init()

audio_path = resource_path(AUDIO_FILE)

pygame.mixer.music.load(audio_path)
pygame.mixer.music.set_volume(VOLUME)

def tocar_audio():
    pygame.mixer.music.play()

def on_click(x, y, button, pressed):
    if pressed:
        if random.random() < CHANCE:
            tocar_audio()

with Listener(on_click=on_click) as listener:
    listener.join()