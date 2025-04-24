import random
from creatures import *


class Participant:
    def __init__(self, name, nickname, favorite_creature, victory):
        self.name = name
        self.nickname = nickname
        self.favorite_creature = favorite_creature
        self.victory = victory

class School:
    def __init__(self, school_name, participant,creatures):
        self.school_name = school_name
        self.list_creature = []

p1 = Participant("Pepper","L'explorateur culinaire",creature3.name,random.randint(1,20))
p2 = Participant("Jacq","Le prof de biologie énergique",creature6.name,random.randint(1,20))
p3 = Participant("Alisma","La présidente de la Ligue Pokémon",creature9,random.randint(1,20))
p4 = Participant("Elise","La surdouée des humanités",creature12.name,random.randint(1,20))

school1 = School("Académie des Arcanes Éternelles",p1,[creature1,creature2,creature3])
school2 = School("École des Maîtres Invocateurs",p2,[creature4,creature5,creature6])
school3 = School("Institut des Arts Occultes",p3,[creature7,creature8,creature9])
school4 = School("Collège des Envouteurs",p4,[creature10,creature11,creature12])

print(p1.favorite_creature)
creature10.creature_presentation()