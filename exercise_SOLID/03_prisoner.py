class Person:

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner:
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        self.is_free = False
        self.position = Prisoner.PRISON_LOCATION

prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
