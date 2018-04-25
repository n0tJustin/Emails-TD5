
# Ninja Mangos
# Mensun Wang,Jonathan,Justin
# Email Tower Defense 5

from gamelib import *
import time
from coords import getCoords

game = Game(700, 520, "Emails Tower's Defense 5")
bk = Image("Images\\background.png", game)
game.setBackground(bk)

starting_screen = Image("Images\\start_screen.png", game)
wood = Image("Images\\wood.png", game)
wood.moveTo(645, 13)
heart1 = Image("Images\\heart.png", game)
heart1.moveTo(670, 20)
heart1.visible = True
heart2 = Image("Images\\heart.png", game)
heart2.moveTo(645, 20)
heart2.visible = True
heart3 = Image("Images\\heart.png", game)
heart3.moveTo(620, 20)
heart3.visible = True
pop = Animation("Images\\pop.png", 4, game, 870 / 2, 600 / 2)
pop.resizeBy(-80)
pop.visible = False
starting_screen.resizeTo(700, 520)

intro = Image("Images\\intro.png", game)
intro.resizeTo(game.width, game.height)

email = Image("Images\\email.png", game)
email.moveTo(620, 405)
email.resizeBy(-50)

inst = Image("Images\\Instructions.png", game)
inst.moveTo(350, 100)

play = Image("Images\\play.png", game)
play.moveTo(635, 470)
play.resizeBy(-25)

title = Image("Images\\start_screen.png", game)
title.resizeTo(game.width, game.height)
emailS = Image("Images\\emailSingle.png", game)
emailInvis = Image("Images\\emailInvis.png", game)
emailInvis.visible = False

win = Image("Images\\win.png", game)
win.resizeBy(50)
end = Image("Images\\end.png", game)
end.resizeBy(65)

wall = Image("Images\\wall.jpg", game)
wall.resizeBy(1000)
wall.visible = False
end.visible = False

win1 = Image("Images\\win1.png",game)
win1.moveTo(350,200)
win1.resizeBy(-50)

win2 = Image("Images\\win2.png",game)
win2.moveTo(350, 240)
win2.resizeBy(-50)

win3 = Image("Images\\win3.png",game)
win3.moveTo(350,260)
win3.resizeBy(-50)

lose1 = Image("Images\\lose1.png",game)
lose1.moveTo(350,300)
lose1.resizeBy(-50)

lose2 = Image("Images\\lose2.png",game)
lose2.moveTo(350,350)
lose2.resizeBy(-5)


emailsHit = 0

snipers = []
for index in range(200):
   snipers.append(Image("Images\\sniper.png", game))
for index in range(200):
   s = randint(10,15)
   x = randint(1, 700)
   y = randint(500, 30000)
   snipers[index].setSpeed(s, 360)
   snipers[index].rotateBy(360)
   snipers[index].moveTo(x, y)
   snipers[index].visible = True

supers = []
for index in range(200):
   supers.append(Image("Images\\super.png", game))
for index in range(200):
   s = randint(25,30)
   x = randint(500, 60000)
   y = randint(1, 520)
   supers[index].setSpeed(s, 0)
   supers[index].rotateBy(270)
   supers[index].moveTo(x, y)
   supers[index].visible = True

popping = Sound("Sounds\\popping.ogg", 1)
oof = Sound("Sounds\\oof.wav", 2)
lose = Sound("Sounds\\lose.ogg", 3)


# starting screen
while not game.over:
   game.processInput()
   title.draw()
   play.draw()

   if play.collidedWith(mouse) and mouse.LeftClick:
       game.over = True
   game.update(30)
game.over = False

while not game.over:
   game.processInput()
   intro.draw()
   email.draw()
   inst.draw()
   play.draw()
   play.moveTo(100, 455)
   win1.draw()
   win2.draw()
   win3.draw()
   lose1.draw()
   lose2.draw()
   if play.collidedWith(mouse) and mouse.LeftClick:
       game.over = True

   game.update(30)
game.over = False


def sniperMover(emailX):
   global emailsHit
   global gameOverEnd
   for index in range(100):
       snipers[index].move()
       if snipers[index].collidedWith(emailX):
           emailsHit += 1
           snipers[index].visible = False
           pop.visible = True
           pop.moveTo(emailX.x, emailX.y)
           if emailsHit == 1:
               heart1.visible = False
               pygame.mixer.music.pause()
               popping.play()
               pygame.mixer.music.unpause()
           if emailsHit == 2:
               heart2.visible = False
               pygame.mixer.music.pause()
               popping.play()
               pygame.mixer.music.unpause()
           if emailsHit == 3:
               heart3.visible = False
               pygame.mixer.music.pause()
               popping.play()
               oof.play()
               pygame.mixer.music.unpause()
               game.stopMusic()
               wall.visible = True
               end.visible = True
               lose.play()
                  


def superMover(emailX):
   global emailsHit
   for index in range(100):
       supers[index].move()
       if supers[index].collidedWith(emailX):
           emailsHit += 1
           supers[index].visible = False
           pop.visible = True
           pop.moveTo(emailX.x, emailX.y)
           if emailsHit == 1:
               heart1.visible = False
               pygame.mixer.music.pause()
               popping.play()
               pygame.mixer.music.unpause()
           if emailsHit == 2:
               heart2.visible = False
               pygame.mixer.music.pause()
               popping.play()
               pygame.mixer.music.unpause()
           if emailsHit == 3:
               heart3.visible = False
               pygame.mixer.music.pause()
               popping.play()
               oof.play()
               pygame.mixer.music.unpause()
               game.stopMusic()
               wall.visible = True
               end.visible = True
               lose.play()


def drawHeart():
   if heart1.visible:
       heart1.draw()
   if heart2.visible:
       heart2.draw()
   if heart3.visible:
       heart3.draw()




def playGame1(coords):
   keepRunning = True
   idx = 0;
   x = 0;
   y = 0
   size = len(coords)

   while keepRunning:
       if idx == size:
           keepRunning = False
       else:
           if not keys.Pressed[K_SPACE]:
               x, y = coords[idx]
               idx += 1

           game.processInput()
           bk.draw()
           wood.draw()
           drawHeart()
           game.drawText("Wave 1", 623, 32, Font(red,24))
           if keys.Pressed[K_SPACE]:
              emailS.visible = False
              emailInvis.visible = True
              emailInvis.moveTo(emailS.x, emailS.y)
           else:
              emailS.visible = True
              emailInvis.visible = False
           emailS.moveTo(x, y)
           sniperMover(emailS)
           wall.draw()
           end.draw()
           emailInvis.draw()
           game.update(30)
           time.sleep(0.03)

def playGame2(coords):
   keepRunning = True
   idx = 0;
   x = 0;
   y = 0
   size = len(coords)

   while keepRunning:
       if idx == size:
           keepRunning = False
       else:
           if not keys.Pressed[K_SPACE]:
               x, y = coords[idx]
               idx += 1

           game.processInput()
           bk.draw()
           wood.draw()
           drawHeart()
           game.drawText("Wave 2", 623, 32, Font(red,24))
           if keys.Pressed[K_SPACE]:
              emailS.visible = False
              emailInvis.visible = True
              emailInvis.moveTo(emailS.x, emailS.y)
           else:
              emailS.visible = True
              emailInvis.visible = False
           emailS.moveTo(x, y)
           superMover(emailS)
           wall.draw()
           end.draw()
           emailInvis.draw()
           game.update(30)
           time.sleep(0.03)

def playGame3(coords):
   keepRunning = True
   idx = 0;
   x = 0;
   y = 0
   size = len(coords)

   while keepRunning:
       if idx == size:
           keepRunning = False
       else:
           if not keys.Pressed[K_SPACE]:
               x, y = coords[idx]
               idx += 1

           game.processInput()
           bk.draw()
           wood.draw()
           drawHeart()
           game.drawText("Wave 3", 623, 32, Font(red,24))
           if keys.Pressed[K_SPACE]:
              emailS.visible = False
              emailInvis.visible = True
              emailInvis.moveTo(emailS.x, emailS.y)
           else:
              emailS.visible = True
              emailInvis.visible = False
           emailS.moveTo(x, y)
           superMover(emailS)
           sniperMover(emailS)
           wall.draw()
           end.draw()
           emailInvis.draw()
           game.update(30)
           time.sleep(0.03)

# lvl 1
game.setMusic("Sounds\\wii_tanks_red.ogg")
pygame.mixer.music.play(9)  # plays 10 times

playGame1(getCoords())

game.update(30)
game.over = False
game.stopMusic()

# lvl 2
game.setMusic("Sounds\\wii_tanks_green.ogg")
pygame.mixer.music.play(9)
if heart3.visible:

   playGame2(getCoords())

   game.update(30)
game.over = False
game.stopMusic()

#lvl 3
game.setMusic("Sounds\\wii_tanks_boss.ogg")
pygame.mixer.music.play(9)
if heart3.visible:
   game.drawText("Wave 2", 300, 300)

   playGame3(getCoords())

   game.update(30)
game.over = False
game.stopMusic()

gameEnder = 0

#win
while not game.over and heart3.visible:
   wall.visible = True
   wall.draw()
   win.draw()
   gameEnder += 1
   if gameEnder >= 100:
      game.over = True
   game.update(30)
game.quit()
