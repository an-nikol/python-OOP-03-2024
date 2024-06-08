from project_1.animal import Animal
from project_1.bear import Bear
from project_1.gorilla import Gorilla
from project_1.lizard import Lizard
from project_1.mammal import Mammal
from project_1.reptile import Reptile
from project_1.snake import Snake

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
