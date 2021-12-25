class Terrain:

    def __init__(self, name, is_walkable):
        self.is_walkable = is_walkable
        self.name = name

    def step_on(self, unit):
        pass

    def can_walk_on(self) -> bool:
        return self.is_walkable

    def get_terrain(self) -> str:
        return self.name


class Door(Terrain):

    def __init__(self):
        super().__init__("Door", True)

    def step_on(self, unit):
        if unit.got_key:
            unit.escaped = True
            print("The hero has escaped! Game over!")


class Grass(Terrain):

    def __init__(self):
        super().__init__("Grass", True)

    def step_on(self, unit):
        print("Such a pleasure walking on fresh grass")


class Key(Terrain):

    def __init__(self):
        super().__init__("Key", True)

    def step_on(self, unit):
        unit.got_key = True


class Trap(Terrain):
    def __init__(self):
        super().__init__("Trap", True)

    def step_on(self, unit):
        unit.get_damage(5)


class Wall(Terrain):

    def __init__(self):
        super().__init__("Wall", False)

