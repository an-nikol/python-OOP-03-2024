from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    # helper properties
    @property
    def __valid_equipment_type(self):
        return {
            "KneePad": KneePad,
            "ElbowPad": ElbowPad
        }

    @property
    def __valid_team_type(self):
        return {
            "OutdoorTeam": OutdoorTeam,
            "IndoorTeam": IndoorTeam
        }

    @staticmethod
    def __find_team_object(searched_item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == searched_item:
                return obj

    @ staticmethod
    def __find_type_of_eq(eq_type: str, collection):
        collection = [eq for eq in collection if eq.TYPE_ == eq_type]
        return collection[-1] if collection else None

    def add_equipment(self, equipment_type: str):
        # check if eq is not valid
        if equipment_type not in self.__valid_equipment_type:
            raise Exception("Invalid equipment type!")

        # create and add the eq
        new_eq = self.__valid_equipment_type[equipment_type]()
        self.equipment.append(new_eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        # check if the team is valid
        if team_type not in self.__valid_team_type:
            raise Exception("Invalid team type!")

        # check if there is available tournament capacity
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        # create and add a team
        new_team = self.__valid_team_type[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        curr_eq_object = self.__find_type_of_eq(equipment_type, self.equipment)
        curr_team_obj = self.__find_team_object(team_name, "name", self.teams)

        # check when the eq cannot be sold to the team
        if curr_eq_object.price > curr_team_obj.budget:
            raise Exception("Budget is not enough!")

        # check when the eq can be sold to the team
        self.equipment.remove(curr_eq_object)
        curr_team_obj.equipment.append(curr_eq_object)
        curr_team_obj.budget -= curr_eq_object.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        curr_team_obj = self.__find_team_object(team_name, "name", self.teams)

        # check if there is a team in the tournament collection
        if not curr_team_obj:
            raise Exception("No such team!")

        # check if the team has any wins
        if curr_team_obj.wins:
            raise Exception(f"The team has {curr_team_obj.wins} wins! Removal is impossible!")

        # successfully remove the team
        self.teams.remove(curr_team_obj)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if eq.TYPE_ == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        # check if all teams are one of the same type
        first_team = self.__find_team_object(team_name1, "name", self.teams)
        second_team = self.__find_team_object(team_name2, "name", self.teams)

        # if both teams are of different types
        if not first_team.TYPE_ == second_team.TYPE_:
            raise Exception("Game cannot start! Team types mismatch!")

        # start the game
        first_team_result = first_team.advantage + sum([eq.protection for eq in first_team.equipment])
        second_team_result = second_team.advantage + sum([eq.protection for eq in second_team.equipment])

        if first_team_result > second_team_result:
            first_team.win()
            return f"The winner is {first_team.name}."
        elif first_team_result < second_team_result:
            second_team.win()
            return f"The winner is {second_team.name}."
        elif first_team_result == second_team_result:
            return "No winner in this game."

    def get_statistics(self):
        output = [f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:"]

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)

        for t in sorted_teams:
            output.append(t.get_statistics())

        return "\n".join(output)

