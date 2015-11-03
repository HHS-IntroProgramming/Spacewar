"""
spaceshooter.py
Author: Adam Pikielny
Credit: Morgan
ggame documentation
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position, app):
        super().__init__(SpaceShip.asset, position)
        self.vx = .0001
        self.vy = .0001
        self.vr = 0
        self.app = app
        #self.vr = math.atan(self.vy/self.vx)
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.moveleft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.moveright)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.moveup)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.movedown)
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
        #if self.collidingWith(sun)==True:
            #self.stop

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation = self.vr
        #is the below function in the write step?
        #if collidingWithSprites(self)==True:
            #print("collision")
        if self.collidingWith(self.app.sun)==True:
            self.stop()
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def moveleft(self, event):
        self.vx += -.1
        self.vr += .01
    def moveright(self, event):
        self.vx += .1
        self.vr += -.01
    def movedown(self, event):
        self.vy += .1
    def moveup(self, event):
        self.vy += -.1

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    def stop(self):
        self.vx=0
        self.vy=0



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #bg_asset = RectangleAsset(width, height, noline, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg=Sprite(bg_asset,(0,0))
        sun_asset = ImageAsset("images/sun.png",Frame(227,0,292-227,125), 4, 'vertical')
        self.sun=Sprite(sun_asset, (200,200))
        SpaceShip((100,100), self)
        #SpaceShip((150,150))
        #SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()