from project_1.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if Pokemon.pokemon_details(pokemon) not in self.pokemons:
            self.pokemons.append(Pokemon.pokemon_details(pokemon))
            return f"Caught {Pokemon.pokemon_details(pokemon)}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for poke_data in self.pokemons:
            if pokemon_name in poke_data:
                self.pokemons.remove(poke_data)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pok_details in self.pokemons:
            result += f"- {pok_details}"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
