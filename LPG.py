import random
import LPD
import sys
from functions import flist,enemies,lovers,rbpath,RoleChoice
nl = '\n'

def runlifepath():
    """Reruns Lifepath results so that to be logged later on
    i changed this so it returns a string instead of printing directly into the file"""

    return f"""your cultural origin is {random.choice(LPD.Corigin)}
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
    ---------------------- ROLE  ------------------------------
    {rbpath()}
    """

ostdout = sys.stdout

with open(f"Lifepath.txt","w") as f :
    text_string= runlifepath() #you generate the text string here
    sys.stdout = f #you change the default output to the file
    print(text_string) #you print shit into the file
    sys.stdout = ostdout #idk what this does but hey, it works