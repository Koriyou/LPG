# this is the main app
from functions import *
import random
import os
import sys

# Helper to get resource path for PyInstaller compatibility
def resource_path(relative_path):
    # PyInstaller sets the _MEIPASS attribute, but it's a convention, not a strict rule
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(""))
    return os.path.join(base_path, relative_path)

nl = '\n'
try:
    with open(resource_path('malenames.txt'), 'r', encoding='utf-8') as file:
        RandomMaleNames = file.read().split('\n')
    with open(resource_path('FemaleNames.txt'), 'r', encoding='utf-8') as file:
        RandomFemaleNames = file.read().split('\n')
except (OSError, IOError) as e:
    print(f"Error loading name files: {e}")
    RandomMaleNames = ["Unknown"]
    RandomFemaleNames = ["Unknown"]


def questionnaire(*args):
    answers = [*args]
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
    if int(answers[1]) >= 11:
        answers[1] = random.randint(1, 10)
    func = Roles.get((int(answers[1])))

    return(f"""# Name : {answers[0]}
## Role : {func()}
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
    - {random.choice(LPD.lg)}""")


with open("LP2.md", "w", encoding='utf-8') as f:
    name = ''
    name = input("what is your name ? press Enter for Random name").strip()
    if name == '':
        while True:
            gender = input(
                "is your character Male or Female ? , Press Enter for Random").strip().lower()
            if gender == "male":
                name = random.choice(RandomMaleNames)
                break
            elif gender == "female":
                name = random.choice(RandomFemaleNames)
                break
            elif gender == '':
                c1 = random.choice(RandomMaleNames)
                c2 = random.choice(RandomFemaleNames)
                choices = [c1, c2]
                name = random.choice(choices)
                break
            else:
                print('choose male or female')
                continue
    # Role input with validation
    while True:
        try:
            role_input = input("""What is your role ? :\n        - choose 1 for Rockerboy\n        - choose 2 for Solo\n        - choose 3 for Netrunner\n        - choose 4 for Tech\n        - choose 5 for Medtech\n        - choose 6 for Media\n        - choose 7 for Exec\n        - choose 8 for Lawman\n        - choose 9 for Fixer\n        - choose 10 for nomad\n        - choose 11 for random role""")
            role_num = int(role_input.strip())
            if 1 <= role_num <= 11:
                break
            else:
                print("Please enter a number between 1 and 11.")
        except ValueError:
            print("Please enter a valid number.")
    f.write(questionnaire(name, role_num))

input("Press Enter to save and exit")
