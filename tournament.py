import time
from utils import *



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

    def fight_turn_player(self,first_player,second_player):
        print(f"{first_player} attaque")
        attack = roll_dice()
        print(attack)
        defense =roll_dice()
        print(defense)
        if attack > defense:
            print("L'attaque a réussi!!!")
            # player2 perd hp
        elif defense > attack:
            print("L'attaque a été parée!!!")
        else:
            print("Egalité!!!")
            self.fight_turn_player(first_player,second_player)

    def fight_turn(self,first_fighter, player1,player2):
        if first_fighter == 1:
            self.fight_turn_player(player1,player2)
            self.fight_turn_player(player2,player1)
        else:
            self.fight_turn_player(player2,player1)
            self.fight_turn_player(player1, player2)

    def fight(self,player1,player2):
        turn = 5
        first_fighter = random.randint(1,2)
        print(first_fighter)
        time.sleep(3)
        while turn > 0:
            self.fight_turn(first_fighter,player1,player2)
            turn -= 1





tournament = Tournament()
tournament.show_title()
time.sleep(2)
print("Bienvenue à l'Academie des Invocateurs !!!")
# playsound('C:/Users/s_13508_dev/PycharmProjects/PythonProject/CreatureTournament/Sounds/cinematic-intro-6097.mp3')
# time.sleep(11)
print("Que le combat commence !!!")
playsound('C:/Users/s_13508_dev/PycharmProjects/PythonProject/CreatureTournament/Sounds/fight.mp3')
time.sleep(5)
tournament.fight("Xavier","J-M")

