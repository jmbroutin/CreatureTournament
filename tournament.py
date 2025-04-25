import time
from copy import deepcopy
from utils import *
from participant import *



class Tournament:
    def __init__(self):
        self.name = "L'Academie  des Invocateurs"
        self.first_semi_final = []
        self.second_semi_final = []
        self.small_final = []
        self.final = []
        self.ranking = []

    def show_title(self):
        show_title(self.name)

    def fight_turn_player(self,turn,first_player,second_player):
        if first_player.hp >0:
            print(f"{first_player.name} attaque")
            attack = roll_dice()
            print(attack)
            defense =roll_dice()
            print(defense)
            if attack > defense:
                print("L'attaque a réussi!!!")
                if turn == 2:
                    print("Attaque spéciale")
                    first_player.lose_life(first_player,second_player,turn)
                    print(second_player.hp)
                else:
                    print("Attaque normale")
                    first_player.lose_life(first_player, second_player, turn)
                    print(second_player.hp)
            elif defense > attack:
                print("L'attaque a été parée!!!")
            else:
                print("Egalité!!!")
                self.fight_turn_player(turn,first_player,second_player)

    def fight_turn(self,first_fighter,turn,player1,player2):
        if first_fighter == 1:
            self.fight_turn_player(turn,player1,player2)
            if player2.hp > 0:
                self.fight_turn_player(turn,player2,player1)
        else:
            self.fight_turn_player(turn,player2,player1)
            if player1.hp > 0:
                self.fight_turn_player(turn,player1, player2)

    def fight(self,player1,player2):
        turn = 5
        first_fighter = random.randint(1,2)
        print(first_fighter)
        time.sleep(3)
        while turn > 0:
            if player1.hp == 0 or player2.hp == 0:
                break
            print(f"----------------{turn}-------------------")
            self.fight_turn(first_fighter, turn, player1, player2)
            turn -= 1
        if player1.hp != player2.hp and player1.hp > player2.hp:
            print(f"{player1.name} est vainqueur")
            return player1
        elif player1.hp != player2.hp and player2.hp > player1.hp:
            print(f"{player2.name} est vainqueur")
            return player2
        elif player1.hp == player2.hp:
            print("Egalité !!! Le combat continue !!!")
            return self.fight(player1,player2)
        else:
            print("Other case")

tournament = Tournament()
tournament.show_title()
time.sleep(2)
print("Bienvenue à l'Academie des Invocateurs !!!")
# playsound('C:/Users/s_13508_dev/PycharmProjects/PythonProject/CreatureTournament/Sounds/cinematic-intro-6097.mp3')
# time.sleep(11)

# Choix des écoles pour la première demi-finale
tournament.first_semi_final.append(random.choice(tournament_school_list))
tournament_school_list.remove(tournament.first_semi_final[0])
tournament.first_semi_final.append(random.choice(tournament_school_list))
tournament_school_list.remove(tournament.first_semi_final[1])

# Choix des écoles pour la deuxième demi-finale
tournament.second_semi_final.append(random.choice(tournament_school_list))
tournament_school_list.remove(tournament.second_semi_final[0])
tournament.second_semi_final.append(random.choice(tournament_school_list))
tournament_school_list.remove(tournament.second_semi_final[1])

print("-----Première demi-finale-----\n")
for i, school in enumerate(tournament.first_semi_final):
    print(f"{school.school_name} \n")
print("-----Deuxième demi-finale-----\n")
for i, school in enumerate(tournament.second_semi_final):
    print(f"{school.school_name} \n")

# Attribution des créatures et Présentation (participants et créatures)

# Première demi-finale
first_semi_final_creatures = [random.choice(tournament.first_semi_final[0].creatures),random.choice(tournament.first_semi_final[1].creatures)]
first_semi_final_creatures_hp = (first_semi_final_creatures[0].hp,first_semi_final_creatures[1].hp)

creature_winner1 = tournament.fight(first_semi_final_creatures[0],first_semi_final_creatures[1])
print(type(creature_winner1))
print(f"{creature_winner1.name} a gagné le combat")
for i,school in enumerate(tournament.first_semi_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner1 == creature:
            print(f"{school.school_name} avance en finale")
            tournament.final.append(school)
            tournament.first_semi_final.remove(school)
            tournament.small_final.append(tournament.first_semi_final[0])

print("------liste petite finale-----")
print(len(tournament.small_final))
print("-----liste finale-----")
print(len(tournament.final))

#Reaffectation des hp après combat
first_semi_final_creatures[0].hp = first_semi_final_creatures_hp[0]
first_semi_final_creatures[1].hp = first_semi_final_creatures_hp[1]

# Deuxième demi-finale
second_semi_final_creatures = [random.choice(tournament.second_semi_final[0].creatures),random.choice(tournament.second_semi_final[1].creatures)]
second_semi_final_creatures_hp = (second_semi_final_creatures[0].hp,second_semi_final_creatures[1].hp)

creature_winner2 = tournament.fight(second_semi_final_creatures[0],second_semi_final_creatures[1])
print(type(creature_winner2))
print(f"{creature_winner2.name} a gagné le combat")
for i,school in enumerate(tournament.second_semi_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner2 == creature:
            print(f"{school.school_name} avance en finale")
            tournament.final.append(school)
            tournament.second_semi_final.remove(school)
            tournament.small_final.append(tournament.second_semi_final[0])

#Reaffectation des hp après combat
second_semi_final_creatures[0].hp = second_semi_final_creatures_hp[0]
second_semi_final_creatures[1].hp = second_semi_final_creatures_hp[1]

print("------liste petite finale-----")
print(len(tournament.small_final))
print("-----liste finale-----")
print(len(tournament.final))

# Petite finale
small_final_creatures = [random.choice(tournament.small_final[0].creatures),random.choice(tournament.small_final[1].creatures)]
small_final_creatures_hp = (small_final_creatures[0].hp,small_final_creatures[1].hp)

creature_winner3 = tournament.fight(small_final_creatures[0],small_final_creatures[1])
print(type(creature_winner3))
print(f"{creature_winner3.name} a gagné le combat")
for i,school in enumerate(tournament.small_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner3 == creature:
            print(f"{school.school_name} gagne la petite finale")
            tournament.ranking.append((school.school_name,3))
            tournament.small_final.remove(school)
            tournament.ranking.append((tournament.small_final[0].school_name,4))

# Grande finale
final_creatures = [random.choice(tournament.final[0].creatures),random.choice(tournament.final[1].creatures)]
final_creatures_hp = (final_creatures[0].hp,final_creatures[1].hp)

creature_winner4 = tournament.fight(final_creatures[0],final_creatures[1])
print(type(creature_winner4))
print(f"{creature_winner4.name} a gagné le combat")
for i,school in enumerate(tournament.final):
    for j, creature in enumerate(school.creatures):
        if creature_winner4 == creature:
            print(f"{school.school_name} est le grand vainqueur du tournoi")
            tournament.ranking.append((school.school_name, 1))
            tournament.final.remove(school)
            tournament.ranking.append((tournament.final[0].school_name, 2))
            # tournament.final.append(school)
#     else:
#         print(f"{school.school_name} fini à la deuxième place")
#         break
#
#
print(tournament.ranking)
print("------Classement Final-----\n")
print(f"1.{tournament.ranking[2]}\n2.{tournament.ranking[3]}\n3.{tournament.ranking[0]}\n4.{tournament.ranking[1]}")
