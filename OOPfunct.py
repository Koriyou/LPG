import random
import LPD
 
def roll():
    """Uses the cyberpunk red formula 1d10-7 to define friends enemies and lovers
    """
    return (random.randint(1, 10)-7)


def flist():
    """Uses the formula in roll()  loop yield friends
    """
    rr = roll()
    if rr <= 0:
        yield "\n        - none"

    for i in range(0, rr):
        yield f"\n        - {random.choice(LPD.Friends)}\n"


def enemies():
    rr = roll()
    if rr <= 0:
        yield "\n        - none"
    for i in range(0, rr):
        yield(f"""\n        - This enemy is {random.choice(LPD.Enemies)}
        	- they hates you for this reason {random.choice(LPD.cause)}
        	- they have the following means at their disposal {random.choice(LPD.throw)}
        	- Their revenge plan is {random.choice(LPD.ven)}\n""")


def lovers():
    rr = roll()
    if rr <= 0:
        yield "\n        - none"
    for i in range(0, rr):
        yield f"\n        - {random.choice(LPD.lovers)}\n"


def newline(text, stringToAppend):
    """this is the mdrasa function"""
    return text+stringToAppend+"\n"  # we append the new string to the general text, the \n stand for a new line


def AnswerInspector(UserInput,AcceptedInputList):
    return UserInput in AcceptedInputList

def AnswerEnforcer(inputMessage,AcceptedInputList=["1","2"]):
    userInput = input(inputMessage)
    while (not AnswerInspector(userInput,AcceptedInputList) ):
         userInput = input("""The Only accepted replies are : """+str(AcceptedInputList))
    return userInput

def Rockerpath():
    path={}
    path['Role Title']="RockerBoy"
    typeOfRockerboy={}
    Rpathresult = AnswerEnforcer("""are you a solo or  are you in a group?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        typeOfRockerboy[0]="you are solo"
        answer = int(AnswerEnforcer("were you once in a group ? 1 yes 2 no"))
        if answer == 1:
            typeOfRockerboy[1]= f"""- you left the group because {random.choice(LPD.ReasonYouLeft)}"""
    elif int(Rpathresult) == 2:
        typeOfRockerboy[0]="""you are in a group"""
    path['type Of Rocker Boy']=typeOfRockerboy
    path['type of venue']=f"""the type of venue you perform in is {random.choice(LPD.TypeOfVenue)}"""
    path['gunners']=f"""the person gunning for you is {random.choice(LPD.Gunning)}"""
    return path

def SoloPath():
    path = {} #empty dick for later insertion
    path["Role Title"] = "Solo"
    path["Type Of Solo"] = f"{random.choice(LPD.SoloType)}"
    path["Moral Compass"] = f"{random.choice(LPD.MoralCompass)}"
    path["Operating Territory"] = f"{random.choice(LPD.OperatingTerritory)}"
    path["Gunners"] = f"{random.choice(LPD.SoloGunning)}"
    return path


def NetrunnerPath():
    path={}
    path["Role Title"]="Netrunner"
    # append the random choice and a new line
    path["typeOfNetrunner"]=f"{random.choice(LPD.TypeOfNetrunner)}"
    Rpathresult = AnswerEnforcer("""Do you have a partner or do you work alone ?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        path['Partner Identity']="you are solo"
    elif int(Rpathresult) == 2:
        path['Partner Identity']=f"- your partner is{random.choice(LPD.PartnerIdentity)}"
    path['Work space']=f"{random.choice(LPD.TypeOfWorkspace)}"
    path['clients']=f"some of your clients are {random.choice(LPD.TypeOfClients)}"
    path['program source']=f"- you get your programs this way :  {random.choice(LPD.ProgramsOrigin)}"
    path['gunners']=f"- Someone is gunning for you  {random.choice(LPD.NetrunnerGunning)}"
    return path


def TechPath():
    path={}
    path["Role Title"] = "Tech"
    # append the random choice and a new line
    TypeOfTech={}
    Rpathresult = AnswerEnforcer("""are you a solo or  are you in a group?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        TypeOfTech[0]="you are solo"
    elif int(Rpathresult) == 2:
        TypeOfTech[0]={random.choice(LPD.TechPartnerIdentity)}
    path['Type Of Tech']=TypeOfTech
    path['Tech Type Of Workspace']=f"{random.choice(LPD.TechTypeOfWorkspace)}"
    path['Tech TypeOfClients']=f"{random.choice(LPD.TechTypeOfClients)}"
    path['Supplies Origin']=f"{random.choice(LPD.SuppliesOrigin)}"
    path['gunners']=f"{random.choice(LPD.TechGunning)}"
    return path

def MedtechPath():
    path={}
    path["Role Title"]="Medtech"
    # append the random choice and a new line
    path["MedtechType"]=f"{random.choice(LPD.MedtechType)}"
    path['MedtechPartner']=f"{random.choice(LPD.MedtechPartner)}"
    path['MedTechTypeOfWorkspace']=f"some of your clients are {random.choice(LPD.MedTechTypeOfWorkspace)}"
    path['MedTechTypeOfClients']=f"- you get your programs this way :  {random.choice(LPD.MedTechTypeOfClients)}"
    path['SuppliesOrigin']=f"- Someone is gunning for you  {random.choice(LPD.SuppliesOrigin)}"
    return path



def MediaPath():
    path={}
    path["Role Title"]="Media"
    # append the random choice and a new line
    path["Media Type"]=f"you are a {random.choice(LPD.MediaType)}"
    path['Publishing mediums']=f"you publish your work via :  {random.choice(LPD.MediaPublications)}"
    path['Ethics']=f"How Ethical are you ? {random.choice(LPD.MediaEthics)}"
    path['Type story']=f"The type of stories you tell are  {random.choice(LPD.MediaStories)}"
    return path


def ExecPath():
    path={}
    path["Role Title"]="Exec"
    # append the random choice and a new line
    path["corpo type"]=f"Corpo type : {random.choice(LPD.CorpoType)}"
    path['corpo devison']=f"{random.choice(LPD.CorpoDivision)}"
    path['Type of Boss']=f"{random.choice(LPD.CorpoAlignement)}"
    path['base of operations']=f"The type of stories you tell are  {random.choice(LPD.MediaStories)}"
    path['gunning']=f"{random.choice(LPD.CorpoGunning)}"
    return path


def LawmanPath():
    path={}
    path["Role Title"]="Lawman"
    # append the random choice and a new line
    path["Position"]=f"Your Position within the force is {random.choice(LPD.LawmanRank)}"
    path['jurisdiction']=f"Your group's jurisdiction is  {random.choice(LPD.LawmanJurisdiction)}"
    path['Group']=f"Your group is {random.choice(LPD.GroupAlignement)}"
    path['gunning']=f"{random.choice(LPD.CorpoGunning)}"
    path['Target Of Choice']=f"Your group's Target of choice is  {random.choice(LPD.GroupTarget)}"
    return path


def FixerPath():
    path={}
    path["Role Title"]="Fixer"
    # append the random choice and a new line
    path["Fixer Type"]=f"You {random.choice(LPD.TypeOfFixer)}"
    path['Group']=f"Your group is {random.choice(LPD.GroupAlignement)}"
    Rpathresult = AnswerEnforcer("""Do you have a partner or do you work alone ?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        path['Partner']="you are solo"
    elif int(Rpathresult) == 2:
        path['Partner']=f"your partner is{random.choice(LPD.FixerPartnerIdentity)}"
    path['Side clients']=f"your side clients are {random.choice(LPD.FixerTypeOfClients)}"
    path['gunners']=f"Someone is gunning for you  {random.choice(LPD.FixerGunning)}"
    return path



def NomadPath(): # the final boss

    path={}
    path["Role Title"] = "Nomad"
    path['Nomad Pack Size'] = f"- Your pack is {random.choice(LPD.NomadPackSize)}"
    # append the random choice and a new line
    TypeOfTech={}
    Rpathresult = AnswerEnforcer("""Where is your tribe based ?
                                 1 for land  2 for air 3 for Sea""",["1","2","3"])
    if int(Rpathresult) == 1:
        path['Land Operations'] = f"{random.choice(LPD.NomadLandOperations)}"
    elif int(Rpathresult) == 2:
        path['Air Operations']= f"{random.choice(LPD.NomadAirOperations)}"
    elif int(Rpathresult) == 3:
        path['Sea Operations']= f"{random.choice(LPD.NomadSeaOperations)}"

    path["Player's Pack Role"]=f"{random.choice(LPD.PlayerPackRole)}"
    path["Pack Philosophy"]=f"{random.choice(LPD.PlayerPackPhilosophy)}"
    path['gunners']=f"{random.choice(LPD.NomadGunning)}"
    return path