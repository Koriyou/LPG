import LPD
import random
from functions import *

nl = '\n'

class Edgerunner():
    def __init__(self,name = None,role =None,lifepath = None,rolebasedlifepath = None):
        self.name = name
        self.role = role
        self.lifepath = lifepath
    def lp (self):
        return f""" ## Lifepath :
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

    def rolebasedlifepath(self,x):
        a = input(("""What is your role ? :
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
        if int(a) >= 11:
            a = random.randint(1, 10)
        func = Roles.get(int(a))
        return func()



Character = Edgerunner("Ali")
Character.lifepath = Character.lp()
Character.role = Character.role()

print(Character.name)
print('-'*10,'Role','-'*10)
print(Character.role)
print('-'*10,'Lifepath','-'*10)
print(Character.lifepath)
print('-'*10,'Role Based Lifepath','-'*10)

print(Character.rolebasedlifepath(2))

