from typing import List

from project_1.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken and people <= room.capacity:
                    room.is_taken = True
                    room.guests = people

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    room.guests = 0

    def status(self):
        total_guests = 0
        for room in self.rooms:
            total_guests += room.guests

        return f"Hotel {self.name} has {total_guests} total guests\n"\
               f"Free rooms: {', '.join(str(room.number)for room in self.rooms if not room.is_taken)}\n"\
               f"Taken rooms: {', '.join(str(room.number)for room in self.rooms if room.is_taken)}\n"