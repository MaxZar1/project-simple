# to jest komentarz
import pgzrun
from random import randint, choice

class Paletka:

    def __init__(self, paletka, pozycja):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]
        self.paletka.odbici = 0

    def add_bounce(self):
        self.paletka.odbic += 1

    def drawing(self):
        self.paletka.draw()

    def move(self, direction):
        if direction == "left":
            self.paletka.x -= 5
        elif direction == "right":
            self.paletka.x += 5

    def bounce(self):
        #taki prosty zabieg nie wystarczy
        if self.paletka.distance_to(ball) > 80:
            return False

        if (self.paletka.y - ball.y) > 20:
            return False


        if self.paletka.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.paletka.x < ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        return True



def aktualizuj_pozycje_paletek():
    if keyboard.a:
        paletka_a.move("left")
    if keyboard.s:
        paletka_a.move("right")
    if keyboard.k:
        paletka_b.move("left")
    if keyboard.l:
        paletka_b.move("right")

def update_ball_position():
    if ball.direction_x == "left":
        ball.x -=ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    if ball.y < 5:
        ball.winner = "GRACZ B"
        ball.stop = True
        ball.game_run = False
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"
        ball.stop = True
        ball.game_run = False

def sprawdz_czy_odbijemy():
    if paletka_a.bounce():
        ball.direction_y = "down"
        paletka_a.add_bounce()
    if paletka_b.bounce():
        ball.direction_y = "up"
        paletka_b.add_bounce()


WIDTH = 1280
HEIGHT = 847

paletka_a = Paletka(Actor("paletka.png"), (100,20))
paletka_b = Paletka(Actor("paletka.png"), (100,830))

ball = Actor("ball-32x32")
ball.x = randint(40,WIDTH - 40)
ball.y = HEIGHT // 2

# dodajemy nasze właściwości
ball.start = False
ball.game_run = False
ball.stop = False
ball.winner = None
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 2


def draw():
    screen.blit("ptak-tlo-1280x847", (0,0))
    if not ball.start:
        screen.draw.text(
            "Naciśnij spacje aby rozpocząć.", (40, 150), fontsize=40, color=(0, 0, 0)
        )
    paletka_a.drawing()
    paletka_b.drawing()
    ball.draw()

def update():
    if not ball.start and keyboard.space:
        ball.game_run = True
        ball.start = True
    if ball.game_run:
        update_ball_position()
        aktualizuj_pozycje_paletek()
        sprawdz_czy_odbijemy()


pgzrun.go()
