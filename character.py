import random
import json

with open('names.json') as f: #opens the Json file
    Names = json.load(f) # Load's json under variable f as variable Names


#we want to put everything we need in one class
class edgeRunner:
  def __init__(self):
    self.setName()
  def setName(self,name=None,sex=None):
      if name is not None:
            self.name=name
      else:
          if sex == "f": #condition is set for argument called in the function.
            name= f'{random.choice(Names)["female"]} {random.choice(Names)["surname"]}'
          elif sex == 'm':
            name= f'{random.choice(Names)["male"]} {random.choice(Names)["surname"]}'
  def generateRole(self,choice=11):
    """unifnished biz"""
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
    if int(choice) >= 11:
        choice = random.randint(1, 10)
  def generateText(self):
      """this is a function to create text"""