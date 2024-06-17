from typing import List

from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

# this is correct

class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    @property
    def __valid_divers(self):
        return {
            'FreeDiver': FreeDiver,
            'ScubaDiver': ScubaDiver,
        }

    @property
    def __valid_fishes(self):
        return {
            'PredatoryFish': PredatoryFish,
            'DeepSeaFish': DeepSeaFish,
        }

    @staticmethod
    def __find_object(searched_item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == searched_item:
                return obj


    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.__valid_divers:
            return f"{diver_type} is not allowed in our competition."

        # check if a diver object with that name is present in the divers list
        diver = self.__find_object(diver_name, "name", self.divers)
        if diver is not None:
            return f"{diver_name} is already a participant."

        # create and add a new diver
        self.divers.append(self.__valid_divers[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.__valid_fishes:
            return f"{fish_type} is forbidden for chasing in our competition."

        # check if a fish object with that name is present in the fish list
        fish = self.__find_object(fish_name, "name", self.fish_list)
        if fish is not None:
            return f"{fish_name} is already permitted."

        # create and add a new fish
        self.fish_list.append(self.__valid_fishes[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        # validate diver
        current_diver = self.__find_object(diver_name, "name", self.divers)
        if not current_diver:
            return f"{diver_name} is not registered for the competition."

        # validate fish
        current_fish = self.__find_object(fish_name, "name", self.fish_list)
        if not current_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        # check zero oxygen level handling
        if current_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # check diver's health
        if current_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # check oxygen level comparison
        if current_diver.oxygen_level < current_fish.time_to_catch:
            current_diver.miss(current_fish.time_to_catch)
            if current_diver.oxygen_level == 0:
                current_diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        elif current_diver.oxygen_level == current_fish.time_to_catch:
            if is_lucky:
                current_diver.hit(current_fish)
                if current_diver.oxygen_level == 0:
                    current_diver.update_health_status()

                return f"{diver_name} hits a {current_fish.points:.1f}pt. {fish_name}."
            else:
                current_diver.miss(current_fish.time_to_catch)
                if current_diver.oxygen_level == 0:
                    current_diver.update_health_status()

                return f"{diver_name} missed a good {fish_name}."
        elif current_diver.oxygen_level > current_fish.time_to_catch:
            current_diver.hit(current_fish)
            if current_diver.oxygen_level == 0:
                current_diver.update_health_status()
            return f"{diver_name} hits a {current_fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        recovered_divers = [d for d in self.divers if d.has_health_issue]
        for diver in recovered_divers:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(recovered_divers)}"

    def diver_catch_report(self, diver_name: str):
        output = [f"**{diver_name} Catch Report**"]

        found_diver = self.__find_object(diver_name, "name", self.divers)

        for caught_fish in found_diver.catch:
            output.append(caught_fish.fish_details())

        return '\n'.join(output)

    def competition_statistics(self):
        output = ["**Nautical Catch Challenge Statistics**"]

        good_hp_condition_divers = [d for d in self.divers if not d.has_health_issue]

        sorted_divers = sorted(good_hp_condition_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        for d in sorted_divers:
            output.append(str(d))

        return "\n".join(output)








