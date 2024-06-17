from project.divers.base_diver import BaseDiver


class ScubaDiver (BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - (time_to_catch * 0.30) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round((time_to_catch * 0.30))

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_LEVEL
