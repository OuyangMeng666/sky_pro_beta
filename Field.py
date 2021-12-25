from Cell import Cell
from Terrain import Grass


class Field:

    def __init__(self, unit, cols, rows):
        self.cols = cols
        self.rows = rows
        self.field = [[0 for x in range(self.rows)] for y in range(self.cols)]
        self.unit = unit

    def cell(self, coordinates):
        return self.field[coordinates[0]][coordinates[1]]

    def move_unit_up(self):
        self._execute_movement(-1, 0)
        print("Moving up!")

    def move_unit_down(self):
        self._execute_movement(1, 0)
        print("Moving down!")

    def move_unit_right(self):
        self._execute_movement(0, 1)
        print("Moving right!")

    def move_unit_left(self):
        self._execute_movement(0, -1)
        print("Moving left!")

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def _execute_movement(self, x, y):
        if self.field[self.unit.get_coordinates()[0] + x][self.unit.get_coordinates()[1] + y]\
                .get_obj().can_walk_on():
            self.field[self.unit.get_coordinates()[0] + x][self.unit.get_coordinates()[1] + y] \
                .get_obj().step_on(self.unit)
            self.draw(self.unit.get_coordinates()[0] + x, self.unit.get_coordinates()[1] + y, self.unit)
            self.draw(self.unit.get_coordinates()[0], self.unit.get_coordinates()[1], Grass())
            self.unit.set_coordinates(self.unit.get_coordinates()[0] + x, self.unit.get_coordinates()[1] + y)
        else:
            print("The hero cannot go through walls")

    def draw(self, x, y, type):
        self.field[x][y] = Cell(type)

