import sys
import time
from copy import deepcopy
from utils import *
from participant import *
from time import sleep


class Tournament:
    def __init__(self):
        self.name = "L'Academie des Invocateurs"
        self.first_semi_final = []
        self.second_semi_final = []
        self.small_final = []
        self.final = []
        self.ranking = []

    def show_title(self):
        show_title(self.name)

    def fight_turn_player(self, turn, first_player, second_player):
        if first_player.hp > 0:
            print(f"\n╔════════════════════════════╗")
            print(f" {first_player.name.center(26)} ")
            print(f"      lance une attaque !  ")
            print(f"╚════════════════════════════╝")

            time.sleep(1)
            print("\n🎲 Jet d'attaque...")
            attack = roll_dice()
            print(f"⚔️ Attaque : {attack}")
            time.sleep(1)

            print("\n🛡 Jet de défense...")
            defense = roll_dice()
            print(f"🛡 Défense : {defense}")
            time.sleep(1)

            if attack > defense:
                print("\n💥 L'attaque a réussi!!!")
                if turn == 2:
                    print("✨ Attaque spéciale!(Tour 4)")
                    first_player.lose_life(first_player, second_player, turn)
                    print(f"❤️ PV de {second_player.name}: {second_player.hp}")
                else:
                    print("💫 Attaque normale")
                    first_player.lose_life(first_player, second_player, turn)
                    print(f"❤️ PV de {second_player.name}: {second_player.hp}")
            elif defense > attack:
                print("\n🔰 La défense a paré l'attaque!!!")
                playsound('Sounds/woshbetter.wav')
                time.sleep(1.5)
            else:
                print("\n⚖️ Égalité!!! Nouvelle tentative...")
                self.fight_turn_player(turn, first_player, second_player)

    def fight_turn(self, first_fighter, turn, player1, player2):
        print(f"\n✦⋆⋅⋆✦⋆⋅⋆✦ Tour {6 - turn} ⋆⋅⋆✦⋆⋅⋆✦")
        time.sleep(0.5)

        if first_fighter == 1:
            self.fight_turn_player(turn, player1, player2)
            if player2.hp > 0:
                self.fight_turn_player(turn, player2, player1)
        else:
            self.fight_turn_player(turn, player2, player1)
            if player1.hp > 0:
                self.fight_turn_player(turn, player1, player2)

    def fight(self, player1, player2):
        print(f"\n⚔️⚔️⚔️ COMBAT: {player1.name} vs {player2.name} ⚔️⚔️⚔️")
        time.sleep(2)

        turn = 5
        first_fighter = random.randint(1, 2)
        print(f"\nLe sort désigne {player1.name if first_fighter == 1 else player2.name} pour attaquer en premier!")
        time.sleep(3)

        while turn > 0:
            if player1.hp == 0 or player2.hp == 0:
                break
            self.fight_turn(first_fighter, turn, player1, player2)
            turn -= 1

        if player1.hp != player2.hp and player1.hp > player2.hp:
            print(f"\n🏆 {player1.name} est vainqueur!")
            return player1
        elif player1.hp != player2.hp and player2.hp > player1.hp:
            print(f"\n🏆 {player2.name} est vainqueur!")
            return player2
        elif player1.hp == player2.hp:
            print("\n⚖️ Égalité !!! Le combat continue !!!")
            time.sleep(2)
            return self.fight(player1, player2)
        else:
            print("\nSituation inattendue!")


# Initialisation du tournoi
tournament = Tournament()
tournament.show_title()
time.sleep(2)
playsound('Sounds/cinematic-intro-6097.mp3')
print("\n✨ Bienvenue à l'Académie des Invocateurs ! ✨")
time.sleep(2)

# Sélection des écoles
print("\n" + "=" * 50)
print("🎲 TIRAGE AU SORT DES ÉCOLES POUR LES DEMI-FINALES")
print("=" * 50)
time.sleep(1)

print("\n🔮 Sélection des écoles pour la première demi-finale...")
time.sleep(2)
tournament.first_semi_final.append(random.choice(tournament_school_list))
print(f"🏛  École sélectionnée: {tournament.first_semi_final[0].school_name}")
time.sleep(1)
tournament_school_list.remove(tournament.first_semi_final[0])

tournament.first_semi_final.append(random.choice(tournament_school_list))
print(f"🏛  École sélectionnée: {tournament.first_semi_final[1].school_name}")
time.sleep(1)
tournament_school_list.remove(tournament.first_semi_final[1])

print("\n🔮 Sélection des écoles pour la deuxième demi-finale...")
time.sleep(2)
tournament.second_semi_final.append(random.choice(tournament_school_list))
print(f"🏛  École sélectionnée: {tournament.second_semi_final[0].school_name}")
time.sleep(1)
tournament_school_list.remove(tournament.second_semi_final[0])

tournament.second_semi_final.append(random.choice(tournament_school_list))
print(f"🏛  École sélectionnée: {tournament.second_semi_final[1].school_name}")
time.sleep(1)
tournament_school_list.remove(tournament.second_semi_final[1])

# Affichage des matchs
print("\n" + "═" * 50)
print("🌟 PROGRAMME DES DEMI-FINALES 🌟")
print("═" * 50)

print("\n🔥 PREMIÈRE DEMI-FINALE 🔥")
for i, school in enumerate(tournament.first_semi_final):
    print(f"⚡ Équipe {i + 1}: {school.school_name}")

print("\n🔥 DEUXIÈME DEMI-FINALE 🔥")
for i, school in enumerate(tournament.second_semi_final):
    print(f"⚡ Équipe {i + 1}: {school.school_name}")
print("═" * 50 + "\n")
time.sleep(3)

# Première demi-finale
print("\n" + "⚡" * 20)
print("⚡ PREMIÈRE DEMI-FINALE ⚡")
print("⚡" * 20)
playsound('Sounds/fight.mp3')

first_semi_final_creatures = [random.choice(tournament.first_semi_final[0].creatures),
                              random.choice(tournament.first_semi_final[1].creatures)]
print(f"\n🧙 {tournament.first_semi_final[0].school_name} envoie: {first_semi_final_creatures[0].name}")
print(f"🧙 {tournament.first_semi_final[1].school_name} envoie: {first_semi_final_creatures[1].name}")
time.sleep(2)

first_semi_final_creatures_hp = (first_semi_final_creatures[0].hp, first_semi_final_creatures[1].hp)
creature_winner1 = tournament.fight(first_semi_final_creatures[0], first_semi_final_creatures[1])

for i, school in enumerate(tournament.first_semi_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner1 == creature:
            print(f"\n🎉 {school.school_name} avance en finale !")
            tournament.final.append(school)
            tournament.first_semi_final.remove(school)
            tournament.small_final.append(tournament.first_semi_final[0])

first_semi_final_creatures[0].hp = first_semi_final_creatures_hp[0]
first_semi_final_creatures[1].hp = first_semi_final_creatures_hp[1]

# Deuxième demi-finale
print("\n" + "⚡" * 20)
print("⚡ DEUXIÈME DEMI-FINALE ⚡")
print("⚡" * 20)
playsound('Sounds/fight.mp3')

second_semi_final_creatures = [random.choice(tournament.second_semi_final[0].creatures),
                               random.choice(tournament.second_semi_final[1].creatures)]
print(f"\n🧙 {tournament.second_semi_final[0].school_name} envoie: {second_semi_final_creatures[0].name}")
print(f"🧙 {tournament.second_semi_final[1].school_name} envoie: {second_semi_final_creatures[1].name}")
time.sleep(2)

second_semi_final_creatures_hp = (second_semi_final_creatures[0].hp, second_semi_final_creatures[1].hp)
creature_winner2 = tournament.fight(second_semi_final_creatures[0], second_semi_final_creatures[1])

for i, school in enumerate(tournament.second_semi_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner2 == creature:
            print(f"\n🎉 {school.school_name} avance en finale !")
            tournament.final.append(school)
            tournament.second_semi_final.remove(school)
            tournament.small_final.append(tournament.second_semi_final[0])

second_semi_final_creatures[0].hp = second_semi_final_creatures_hp[0]
second_semi_final_creatures[1].hp = second_semi_final_creatures_hp[1]

# Petite finale
print("\n" + "🌠" * 20)
print("🌠 PETITE FINALE 🌠")
print("🌠" * 20)
playsound('Sounds/fight.mp3')

small_final_creatures = [random.choice(tournament.small_final[0].creatures),
                         random.choice(tournament.small_final[1].creatures)]
print(f"\n🧙 {tournament.small_final[0].school_name} envoie: {small_final_creatures[0].name}")
print(f"🧙 {tournament.small_final[1].school_name} envoie: {small_final_creatures[1].name}")
time.sleep(2)

small_final_creatures_hp = (small_final_creatures[0].hp, small_final_creatures[1].hp)
creature_winner3 = tournament.fight(small_final_creatures[0], small_final_creatures[1])

for i, school in enumerate(tournament.small_final):
    for j, creature in enumerate(school.creatures):
        if creature_winner3 == creature:
            print(f"\n🥉 {school.school_name} remporte la 3ème place !")
            tournament.ranking.append((school.school_name, 3))
            tournament.small_final.remove(school)
            tournament.ranking.append((tournament.small_final[0].school_name, 4))

small_final_creatures[0].hp = small_final_creatures_hp[0]
small_final_creatures[1].hp = small_final_creatures_hp[1]

# Grande finale
print("\n" + "🌟" * 20)
print("🌟 GRANDE FINALE 🌟")
print("🌟" * 20)
playsound('Sounds/fight.mp3')

final_creatures = [random.choice(tournament.final[0].creatures),
                   random.choice(tournament.final[1].creatures)]
print(f"\n🧙 {tournament.final[0].school_name} envoie: {final_creatures[0].name}")
print(f"🧙 {tournament.final[1].school_name} envoie: {final_creatures[1].name}")
time.sleep(2)

final_creatures_hp = (final_creatures[0].hp, final_creatures[1].hp)
creature_winner4 = tournament.fight(final_creatures[0], final_creatures[1])

for i, school in enumerate(tournament.final):
    for j, creature in enumerate(school.creatures):
        if creature_winner4 == creature:
            print(f"\n🏆 {school.school_name} est le CHAMPION du tournoi !")
            tournament.ranking.append((school.school_name, 1))
            tournament.final.remove(school)
            tournament.ranking.append((tournament.final[0].school_name, 2))

final_creatures[0].hp = final_creatures_hp[0]
final_creatures[1].hp = final_creatures_hp[1]

# Classement final
print("\n" + "⭐" * 50)
print("🏆 CLASSEMENT FINAL DU TOURNOI 🏆")
print("⭐" * 50)
playsound('Sounds/victory.mp3')
time.sleep(2)
print(f"""
🥇 1ère place: {tournament.ranking[2][0]}
🥈 2ème place: {tournament.ranking[3][0]}
🥉 3ème place: {tournament.ranking[0][0]}
4ème place: {tournament.ranking[1][0]}
""")

print("\n✨ Félicitations à tous les participants ! ✨")
print("⭐" * 50)