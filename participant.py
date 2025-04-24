import random


class Participant:
    def __init__(self, name, nickname, favorite_creature, victory):
        self.name = name
        self.nickname = nickname
        self.favorite_creature = favorite_creature
        self.victory = victory

class School:
    def __init__(self, school_name, participant):
        self.school_name = school_name
        self.list_creature = []

p1 = Participant("Pepper","L'explorateur culinaire","",random.randint(1,20))
p2 = Participant("Jacq","Le prof de biologie énergique","",random.randint(1,20))
p3 = Participant("Alisma","La présidente de la Ligue Pokémon","",random.randint(1,20))
p4 = Participant("Elise","La surdouée des humanités","",random.randint(1,20))

school1 = School("Académie des Arcanes Éternelles",p1)
school2 = School("École des Maîtres Invocateurs",p2)
school3 = School("Institut des Arts Occultes",p3)
school4 = School("Collège des Envouteurs",p4)

