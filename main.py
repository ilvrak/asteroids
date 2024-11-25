import sys
import pygame as pg
from constants import *
from screenborders import ScreenBorders
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


class Game:
    def __init__(self):
        pg.init
        self.screen = pg.display.set_mode(SCREEN_RES)
        self.borders = ScreenBorders(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pg.time.Clock()

        self.updatable = pg.sprite.Group()
        self.drawable = pg.sprite.Group()
        self.asteroids = pg.sprite.Group()
        self.shots = pg.sprite.Group()

        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        self.asteroid_field = AsteroidField()

        Player.containers = (self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
            pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self, dt):
        self.updatable.update(dt)
        self.borders.check_bounds(self.player.position)
        for asteroid in self.asteroids:
            if asteroid.collides_with(self.player):
                print('Game over!')
                sys.exit()
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

    def draw(self):
        self.screen.fill('black')
        for obj in self.drawable:
            obj.draw(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
