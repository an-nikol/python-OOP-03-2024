from project_1.hero import Hero
from project_1.elf import Elf
from project_1.muse_elf import MuseElf
from project_1.wizard import Wizard
from project_1.dark_wizard import DarkWizard
from project_1.soul_master import SoulMaster
from project_1.knight import Knight
from project_1.dark_knight import DarkKnight
from project_1.blade_knight import BladeKnight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
