from Cell import Cell
from Field import Field
from Unit import Ghost
from Terrain import *


class GameController:

    def __init__(self, string_field):
        self.string_field = string_field
        self.mapping = {
            'Wall': '🔲',
            'Grass': '⬜️',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }
        self.game_on = True
        self.hero = Ghost("Ghost", 10, [1, 3])
        self.field = Field(self.hero, 10, 10)

    def make_field(self):
        for i in range(self.field.rows):
            for j in range(self.field.cols):
                if self.string_field[0] == "W":
                    self.field.field[i][j] = Cell(Wall())
                elif self.string_field[0] == "g":
                    self.field.field[i][j] = Cell(Grass())
                elif self.string_field[0] == "K":
                    self.field.field[i][j] = Cell(Key())
                elif self.string_field[0] == "D":
                    self.field.field[i][j] = Cell(Door())
                elif self.string_field[0] == "T":
                    self.field.field[i][j] = Cell(Trap())
                elif self.string_field[0] == "G":
                    self.field.field[i][j] = Cell(self.hero)
                self.string_field = self.string_field[1:]

    def show_field(self):
        for i in range(self.field.rows):
            for j in range(self.field.cols):
                print(self.mapping[self.field.field[i][j].get_obj().name], end="", sep=" ")
            print("\n")

    def play(self):
        print("Welcome to the escape room game")
        self.make_field()
        self.show_field()
        while self.hero.is_alive() and self.game_on and not self.hero.escaped:
            print("Please input your command: W for UP, S for DOWN, A for LEFT and D for RIGHT. Stop the game with "
                  "stop command")
            command = input()

            if command == "w":
                self.field.move_unit_up()
                self.show_field()

            elif command == "s":
                self.field.move_unit_down()
                self.show_field()

            elif command == "a":
                self.field.move_unit_left()
                self.show_field()

            elif command == "d":
                self.field.move_unit_right()
                self.show_field()

            elif command == "stop":
                self.game_on = False
                print("Game over")
