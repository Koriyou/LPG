import random
import json
from OOPfunct import *

with open('names.json') as f: #opens the Json file
    Names = json.load(f) # Load's json under variable f as variable Names

#we want to put everything we need in one class
class edgeRunner:
  name=None
  role=None
  def __init__(self):
    self.setName()
    self.generateRole()
    self.show()
  def __str__(self):
     return self.name+str(self.role)
  def setName(self,name=None,sex=None):
      if name is not None:
            self.name=name
      else:
          if sex == "f": #condition is set for argument called in the function.
            self.name= f'{random.choice(Names)["female"]} {random.choice(Names)["surname"]}'
          elif sex == 'm':
            self.name= f'{random.choice(Names)["male"]} {random.choice(Names)["surname"]}'
          else: self.name="3bo khcha fik zbo"
  def generateRole(self,choice=11):
    choice=int(choice)
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
    if choice >= 11:
        choice = random.randint(1, 10)
    func = Roles.get(choice)
    self.role=func()
  def show(self):
      print(str(self))
  def exportToFile(self):
    """# Rhoda Olsen
## Lifepath :
### Personals
- Cultural origin
    - Oceania/Pacific Islander
- Personality
    - Silly and fluff-headed
- Fashion
    - Leisurewear (Comfort, Agility, Athleticism)
    - Wild and all over
    - Spiked gloves
- Values
    - you value Family above all else
    - I stay neutral.
    - the person you value most is: A brother or sister and your most valued possession is A tool
- Family background
    - Corporate Execs:
      - Wealthy powerful with servants luxury homes and the best of everything. Private security made sure you were always safe. You definitely went to a big-name private school.
- Childhood Environnement
    - In a Drift Nation (a floating offshore city) that is a meeting place for all kinds of people.
- Family crisis
    - Your family was killed, and you were the only,survivor.
- Relationships
    - Friends :
        - none
    - Enemies :
        - none
    - former lovers :
        - none
- Life Goal
    - Live down your past life and try to forget it.
 ### Solo
- you are a Bodyguard
- your moral compass is Always working for good, trying to take out the "bad guys."
- you operate in Combat Zones
- Someone is gunning for you A rival Solo who sees you as their nemesis.
"""
    pass


