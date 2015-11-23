"""
spaceshooter.py
Author: Sam Supattapone
Credit: original code

Assignment: Space Shooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time



asset = ImageAsset("images/starfield.jpg")
width = 512
height = 512

stars = Sprite(asset)
stars1 = Sprite(asset)
stars1.x = 512
stars1.y = 0
stars2 = Sprite(asset)
stars2.x = 1024
stars2.y = 0
stars3 = Sprite(asset)
stars3.x = 0
stars3.y = 512
stars4 = Sprite(asset)
stars4.x = 512
stars4.y = 512
stars5 = Sprite(asset)
stars5.x = 1024
stars5.y = 512


app = App()
app.run()
