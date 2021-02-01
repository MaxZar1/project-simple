# to jest komentarz
import pgzrun

class Paletka:

    def __init__(self, paletka, pozycja):
        self.paletka = paletka
        self.paletka.x = pozycja[0]
        self.paletka.y = pozycja[1]

    def drawing(self):
        self.paletka.draw()


WIDTH = 1280
HEIGHT = 847

paletka_a = Paletka(Actor("palette-128x128"), (100,20))
paletka_b = Paletka(Actor("palette-128x128"), (100,830))

def draw():
    screen.blit("ptak-tlo-1280x847", (0,0))
    paletka_a.drawing()
    paletka_b.drawing()

pgzrun.go()
