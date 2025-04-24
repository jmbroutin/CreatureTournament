import random
import pyfiglet
from pygame import mixer

# Display title in ASCII
def show_title(title):
    ascii_art = pyfiglet.figlet_format(title, width=80)
    print("\033[36m" + ascii_art + "\033[0m")  # Cyan

def playsound(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

def roll_dice():
    return random.randint(1,6)