# this is the main app
from functions import *
import random
import json


def randomName(sex):
    """ generate random female or male names at random to be called later on"""
    # import json file
    with open('names.json') as f: #opens the Json file
        Names = json.load(f) # Load's json under variable f as variable Names
    if sex == "f": #condition is set for argument called in the function.
        return f'{random.choice(Names)["female"]} {random.choice(Names)["surname"]}'
    elif sex == 'm':
        return f'{random.choice(Names)["male"]} {random.choice(Names)["surname"]}'
    else:
        return "put the damn sex in the function you ass"


nl = '\n'


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

    return(f"""# {answers[0]}
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


with open("LP2.md", "w") as f:
    name = ''
    name = input("what is your name ? press Enter for Random name \n")
    if name == '':
        while True:
            name = input(
                "is your character Male or Female ? , Press Enter for Random \n").capitalize()
            if name == "Male":
                name = randomName("m") #this here calls the randomName function and passes the string as an argument
                break
            elif name == "Female":
                name = randomName("f")
                break
            elif name == '':
                # either put "m" or "f" in the random name function
                name = randomName(random.choice(["m", "f"]))
                break
            else:
                print('choose male or female')
                continue
    f.write(questionnaire(name, input("""What is your role ? :
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
        - choose 11 for random role \n""")))

input("Press Enter to save and exit")
