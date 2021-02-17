from functions import *
import random

nl = '\n'
file = open('malenames.txt', 'r')
RandomMaleNames = file.read().split('\n')
file.close()

file = open('FemaleNames.txt', 'r')
RandomFemaleNames = file.read().split('\n')
file.close()

def questionnaire(*args):
    answers = [*args]
    Roles = {1:Rockerpath,
            2:SoloPath,
            3:NetrunnerPath,
            4:TechPath,
            5:MedtechPath,
            6:MediaPath,
            7:ExecPath,
            8:LawmanPath,
            9:FixerPath,
            10:NomadPath}
    if int(answers[1]) >= 11:
        answers[1] = random.randint(1,10)
    func = Roles.get((int(answers[1])))

    return(f"""your name is {answers[0]} and {func()}

          -this is your lifepath :

    your cultural origin is {random.choice(LPD.Corigin)}
    you are {random.choice(LPD.personality)}
    your favorite dress code is {random.choice(LPD.dresscode)}
    your favorite hairstyle  is {random.choice(LPD.hairstyle)}
    People always notice your {random.choice(LPD.Aff)}
    you value {random.choice(LPD.Value)} above all else
    when it comes to people this is what you think : {random.choice(LPD.people)}
    the person you value most is: {random.choice(LPD.ValuedPerson)} and your most valued possession is {random.choice(LPD.ValuedPocession)}
    Family background
    {random.choice(LPD.Fbackground)}
    Environnement
    {random.choice(LPD.Environnement)}
    {random.choice(LPD.Crisis)}
    Friends :{nl.join(flist())}
    Enemies :{nl.join(enemies())}
    former lovers :{nl.join(lovers())}
    your lifegoal is : {random.choice(LPD.lg)}

          """)


with open("LP2.txt","w") as f:
    name = ''
    name = input("what is your name ? press Enter for Random name")
    if name == '':
        name = input("is your character Male or Female ?").capitalize()
        if name == "Male":
            name = random.choice(RandomMaleNames)
        if name == "Female":
            name = random.choice(RandomFemaleNames)
    f.write(questionnaire(name,input("""What is your role ? :
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
        - choose 11 for random role""")))

input("Press Enter to save and exit")



