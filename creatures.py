
class Creatures:
    def __init__(self, name, hp, level, attack, special_ability, presentation):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack = attack
        self.special_ability = special_ability
        self.presentation = presentation

    def creature_presentation (self):

        if self.special_ability == "dmg2":
            description_special_ability = "dégâts x2"

        elif self.special_ability == "dmg3":
            description_special_ability = "dégâts x3"

        else:
            description_special_ability = "Mort instantannée de la créature adverse"

        print(f"Je suis {self.name}. {self.presentation}")
        print(f"J'ai {self.hp} points de vie parce que je suis level {self.level} et mon attaque spéciale est: \n⚡ {description_special_ability} \n")


creature1 = Creatures ("Flamouron 🐉", 5, 1, "Brasier final","dmg2"
                      ,"Né des braises d’un volcan endormi, Flamouron crache le feu de l’ancienne colère des dragons.🐉")

creature2 = Creatures ("️Glacelia ❄️", 7, 2, "Givre figé", "dmg3"
                      ,"Glacélia, souffle givré des montagnes éternelles, fige le temps d’un simple battement d’ailes.")

creature3 = Creatures ("Ornifauve 🌪 ", 9, 3, "Rafale sauvage", "kill"
                     , "Tornifauve rugit comme l’orage : imprévisible, rapide, et toujours dévastateur.")

creature4 = Creatures ("Rochombre 🪨", 5, 1, "Cuirasse obscure", "dmg2"
                      ,"Forgé dans les entrailles de la terre, Rochombre veille dans le silence des cavernes obscures.")

creature5 = Creatures ("Voltacorne ⚡", 7, 2, "Impact statique", "dmg3"
                      ,"Voltacorne traverse les champs de bataille comme l’éclair fend le ciel : brutal, net, sans avertissement.")

creature6 = Creatures("Syfideo 🍃", 9, 3, "Lien vital", "kill",
                      "Messager des forêts anciennes, Sylfidéon murmure aux feuilles… et frappe dans l’ombre.")

creature7 = Creatures ("Noctilume 🌙", 5,1, "Vision prophétique", "dmg2"
                     ,"Noctilume voit dans la nuit ce que nul ne devrait voir, et porte la sagesse des étoiles.")

creature8 = Creatures ("Centralisk 🔥", 7,2, "Mure brûlante", "dmg3",
                       "Issu des cendres d’un ancien brasier, Cendralisk rampe avec la chaleur de la vengeance.")

creature9 = Creatures("Aquariel 🌊", 9, 3, "Onde apaisante", "kill",
                      " Aquariel chante avec les courants, mais méfie-toi : même la plus douce des vagues peut noyer. ")

creature10 = Creatures("Toxymetra ☠️", 5, 1, "Peau toxique", "dmg2",
                       " Un souffle, un contact, un regard… et Toxymétra a déjà inoculé son venin.")

creature11 = Creatures("Aeronik 💨", 7, 2, "Trombe chaotique", "dmg3"
                      ,"Invisible, intenable, insaisissable : Aéronik frappe avant que tu ne comprennes d’où vient le vent.")

creature12 = Creatures("Obscurys 👻", 9, 3, "Phasage spectral", "kill",
                       "Obscurys ne vit pas. Il rôde. Entre les ombres. Entre deux mondes.")


creature1.creature_presentation()
creature2.creature_presentation()
creature3.creature_presentation()