<<<<<<< HEAD
class Ball():
    def __init__(self):
        self.xPos = width/2
        self.yPos = height/2
        
    def move():
        xDirection = 1
        yDirection = 1
        speed = 2
        xPos = xPos + ( speed * xDirection )
        yPos = yPos + (speed * yDirection)
        if xpos > width or xpos < 0
        xDirection *= -1 
=======
from paddle import Paddle

xDirection = 1
yDirection = 1

class Ball():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        
    def move(self,screenWidth, screenHeight, players):
        global xDirection
        global yDirection
        speed = 2
        self.xPos = self.xPos - ( speed * xDirection )
        self.yPos = self.yPos - (speed * yDirection)
        if self.xPos > screenWidth or self.xPos < 0:
            xDirection *= -1
        if self.yPos > screenHeight or self.yPos < 0:
            yDirection *= -1 
            
        for player in players:
            if (player.yPos - 10) <= self.yPos <= (player.yPos +10):
                xDirection *= -1
>>>>>>> 205c14527a2143a9fa1d09ea5a123374df81d361

        
    def draw(self):
        fill(247, 0, 0)
        ellipse(self.xPos, self.yPos, 25, 25)
        fill(255, 255, 255)