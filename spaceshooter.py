from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 1000
    height = 600

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class Ship(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        SpaceGame.listenKeyEvent('keydown', 'right arrow', self.rotateRight)
        SpaceGame.listenKeyEvent('keydown', 'left arrow', self.rotateLeft)
        
    def rotateRight(self, event):
        self.rotation -= 1
    def rotateLeft(self, event):
        self.rotation += 1
    
class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Stars((0,0))
        Sun((256,256))
        Ship((100,100))
        

        
        
        
        
    
SpaceGame().run()

