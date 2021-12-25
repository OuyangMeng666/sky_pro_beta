class Unit:

    def __init__(self, hp, coord):
        self.hp = hp
        self.got_key = False
        self.coord = coord
        self.escaped = False

    def has_key(self) -> bool:
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        if damage < self.hp:
            self.hp -= damage
        else:
            self.hp = 0
            raise UnitDied("The hero has died in a trap. RIP")

    def set_coordinates(self, x, y):
        self.coord = [x, y]

    def get_coordinates(self):
        return self.coord

    def has_position(self, x, y):
        return [x, y] == self.coordinates


class Ghost(Unit):

    def __init__(self, name, hp, coord):
        super().__init__(hp, coord)
        self.name = name


class UnitDied(Exception):
    pass

