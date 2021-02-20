import LPD
import random
from functions import *
import json


nl = '\n'

class Edgerunner():
    def __init__(self,name = None,role =None,lifepath = None,rolebasedlifepath = None):
        self.name = name
        self.role = role
        self.lifepath = lifepath
    def lp (self):
        return f"""
## Lifepath :
### Personals
- Cultural origin
    - {random.choice(LPD.Corigin)}
- Personality
    - {random.choice(LPD.personality)}
- Fashion
    - {random.choice(LPD.dresscode)}
    - {random.choice(LPD.hairstyle)}
    - {random.choice(LPD.Aff)}
- Values
    - you value {random.choice(LPD.Value)} above all else
    - {random.choice(LPD.people)}
    - the person you value most is: {random.choice(LPD.ValuedPerson)} and your most valued possession is {random.choice(LPD.ValuedPocession)}
- Family background
    - {random.choice(LPD.Fbackground)}
- Childhood Environnement
    - {random.choice(LPD.Environnement)}
- Family crisis
    - {random.choice(LPD.Crisis)}
- Relationships
    - Friends :{nl.join(flist())}
    - Enemies :{nl.join(enemies())}
    - former lovers :{nl.join(lovers())}
- Life Goal
    - {random.choice(LPD.lg)}"""

    def rbl(self):
        x = input(("""What is your role ? :
            - choose 1 for Rockerboy
            - choose 2 for Solo
            - choose 3 for Netrunner
            - choose 4 for Tech
            - choose 5 for Medtech
            - choose 6 for Media
            - choose 7 for Exec
            - choose 8 for Lawman
            - choose 9 for Fixer
            - choose 10 for nomad
            - choose 11 for random role \n"""))
        Roles = {1: Rockerpath,
                2: SoloPath,
                3: NetrunnerPath,
                4: TechPath,
                5: MedtechPath,
                6: MediaPath,
                7: ExecPath,
                8: LawmanPath,
                9: FixerPath,
                10: NomadPath}
        if int(x) >= 11:
            x = random.randint(1, 10)
        func = Roles.get(int(x))
        return func()

Character = Edgerunner(input("Who are you ? Leave blank for random name\n"))
if Character.name == '':
        sex = input("Male or Female ?\n").capitalize()
        with open('names.json') as f: #opens the Json file
            Names = json.load(f) # Load's json under variable f as variable Names
        if sex == "Female": #condition is set for argument called in the function.
            Character.name = f'{random.choice(Names)["female"]} {random.choice(Names)["surname"]}'
        elif sex == 'Male':
            Character.name = f'{random.choice(Names)["male"]} {random.choice(Names)["surname"]}'
Character.lifepath = Character.lp()
Character.rolebasedlifepath = Character.rbl()


with open("LP2.md", "w") as f:
    f.write(f'# {Character.name}\n{Character.lifepath}\n{Character.rolebasedlifepath}')

input("Exit\n")