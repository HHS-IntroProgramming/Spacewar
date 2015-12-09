from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 775

asset1 = ImageAsset("images/starfield.jpg")
width = 512
height = 512
 
stars = Sprite(asset1)
stars1 = Sprite(asset1)
stars1.x = 512
stars1.y = 0
stars2 = Sprite(asset1)
stars2.x = 1024
stars2.y = 0
stars3 = Sprite(asset1)
stars3.x = 0
stars3.y = 512
stars4 = Sprite(asset1)
stars4.x = 512
stars4.y = 512
stars5 = Sprite(asset1)
stars5.x = 1024
stars5.y = 512

Sprite(asset)

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.turn = 0
        self.go = 0
        self.rotation = 0
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.rotation += self.turn/75
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1
        self.x += -sin(self.rotation)
        self.y += -cos(self.rotation)
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def turnleftOn(self, event):
        self.turn = 1
    
    def turnleftOff(self, event):
        self.turn = 0
    
    def turnrightOn(self, event):
        self.turn = -1
    
    def turnrightOff(self, event):
        self.turn = 0
    
    def goforwardOn(self, event):
        self.go = 1
        
    def goforwardOff(self, event):
        self.go = 0

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ship = SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', myapp.ship.thrustOn)
myapp.listenKeyEvent('keyup', 'space', myapp.ship.thrustOff)
myapp.listenKeyEvent('keydown', 'a', myapp.ship.turnleftOn)
myapp.listenKeyEvent('keyup', 'a', myapp.ship.turnleftOff)
myapp.listenKeyEvent('keydown', 'd', myapp.ship.turnrightOn)
myapp.listenKeyEvent('keyup', 'd', myapp.ship.turnrightOff)
myapp.run()