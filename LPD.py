import math
import random

Corigin = ["North American","South/central American","Western European",
    "Eastern European","Middle Eastern","Sub saharan African","South Asian","South East Asian",
    "East Asian","Oceania/Pacific Islander"]
personality = ["Shy and secretive",
"Rebellious, antisocial, and violent","Arrogant, proud, and aloof","Moody, rash, and headstrong","Picky, fussy, and nervous",
"Stable and serious","Silly and fluff-headed","Sneaky and deceptive","Intellectual and detached","Friendly and outgoing"]
dresscode = ["Generic Chic (Standard, Colorful, Modular)","Leisurewear (Comfort, Agility, Athleticism)","Urban Flash (Flashy, Technological, Streetwear)",
"Businesswear (Leadership, Presence, Authority)","High Fashion (Exclusive, Designer, Couture)","Bohemian (Folksy, Retro, Free-spirited)",
"Bag Lady Chic (Homeless, Ragged, Vagrant)","Gang Colors (Dangerous, Violent, Rebellious)","Nomad Leathers (Western, Rugged, Tribal)",
"Asia Pop (Bright, Costume-like, Youthful)"]
hairstyle = ["Mohawk","Long and ratty","Short and spiked","Wild and all over","Bald","Striped","Wild colors","Neat and short","Short and curly",
"Long and straight"]
Aff = ["Tattoos","Mirrorshades","Ritual scars","Spiked gloves","Nose rings","piercings","Strange fingernail implants",
"Spiked boots or heels","Fingerless gloves","Strange contacts"]
Value = ["Money","Honor","Your word","Honesty","Knowledge","Vengeance","Love","Power","Family","Friendship"]
people = ["I stay neutral.","I stay neutral.","I like almost everyone.","I hate almost everyone.",
"People are tools. Use them for your own goals then discard them.","Every person is a valuable individual.",
"People are obstacles to be destroyed if they cross me.","People are untrustworthy. Don't depend on anyone.",
"Wipe'em all out and let the cockroaches take over.","People are wonderful!"]
ValuedPerson = ["A parent","A brother or sister","A lover","A friend","Yourself","A pet",
"A teacher or mentor","A public figure","A personal hero","No one"]
ValuedPocession = ["A weapon","A tool","A piece of clothing","A photograph","A book or diary","A recording","A musical instrument","A piece of jewelry",
"A toy","A letter"]
Fbackground = ["Corporate Execs: Wealthy powerful with servants luxury homes and the best of everything. Private security made sure you were always safe. You definitely went to a big-name private school.",
    "Corporate Managers : Well to do, with large homes, safe neighborhoods, nice cars, etc. Sometimes your parent(s) would hire servants, although this was rare. You had a mix of private and corporate education. ",
    "Corporate Technicians : Middle-middle class, with comfortable conapts or Beaverville suburban homes, minivans and corporate-run technical schools. Kind of like living 1950s America crossed with 1984. ",
    "Nomad Pack You had a mix of rugged trailers, vehicles, and huge road kombis for your home. You learned to drive and fight at an early age, but the family was always there to care for you. Food was actually fresh and abundant. Mostly home schooled. ",
    "Ganger \"Family\" : A savage, violent home in any place the gang could take over. You were usually hungry, cold, and scared. You probably didn't know who your actual parents were. Education? The Gang taught you how to fight, kill, and steal—what else did you need to know? ",
    "Combat Zoners :  A step up from a gang \"family,\" your home was a decaying building somewhere in the ‘Zone', heavily fortified. You were hungry at times, but regularly could score a bed and a meal. Home schooled. ",
    "Urban Homeless : You lived in cars, dumpsters, or abandoned shipping modules. If you were lucky. You were usually hungry, cold, and scared, unless you were tough enough to fight for the scraps. Education? School of Hard Knocks. ",
    "Megastructure Warren Rats l You grew up in one of the huge new megastructures that went up after the War. A tiny conapt, kibble and scop for food, a mostly warm bed. Some better educated adult warren dwellers or a local Corporation may have set up a school. ",
    "Reclaimers : You started out on the road, but then moved into one of the deserted ghost towns or cities to rebuild it. A pioneer life: dangerous, but with plenty of simple food and a safe place to sleep. You were home schooled if there was anyone who had the time. Edgerunners Your home was always changing based on your parents' current \"job.\" Could be a luxury apartment, an urban conapt, or a dumpster if you were on the run. Food and shelter ran the gamut from gourmet to kibble. "]
Environnement = ["Ran on The Street, with no adult supervision.","Spent in a safe Corp Zone walled off from the rest of the City.",
"In a Nomad pack moving from place to place.","In a Nomad pack with roots in transport (ships, planes, caravans).",
"In a decaying, once upscale neighborhood,now holding off the boosters to survive.",
"In the heart of the Combat Zone, living in a wrecked building or other squat.",
"In a huge \"megastructure\" building controlled by a Corp or the City.","In the ruins of a deserted town or city taken over by Reclaimers.",
"In a Drift Nation (a floating offshore city) that is a meeting place for all kinds of people.",
"In a Corporate luxury \"starscraper,\" high abovethe rest of the teeming rabble."]

Crisis = ["Your family lost everything through betrayal.","Your family lost everything through bad,management.",
"Your family was exiled or otherwise driven from their original home/nation/Corporation.","Your family is imprisoned, and you alone escaped",
"Your family vanished. You are the only,remaining member.","Your family was killed, and you were the only,survivor.",
"Your family is involved in a long-term,conspiracy, organization, or association, such,as a crime family or revolutionary group.",
"Your family was scattered to the winds due to,misfortune.","Your family is cursed with a hereditary feud,that has lasted for generations.",
"You are the inheritor of a family debt; you must,honor this debt before moving on with your life.",]

Friends = ["Like an older sibling to you.","Like a younger sibling to you.","A teacher or mentor.,A partner or coworker."
,"A former lover.","An old enemy.","Like a parent to you.","An old childhood friend.","Someone you know from The Street.",
"Someone with a common interest or goal."]

Enemies = ["Ex-friend,Ex-lover,Estranged relative,Childhood enemy","Person working for you","Person you work for",
"Partner or coworker,Corporate exec","Government official","Boosterganger"]

cause = ["Caused the other to lose face or status.","Caused the loss of lover friend, or relative.","Caused a major public humiliation.",
"Accused the other of cowardice or some other,major personal flaw.","Deserted or betrayed the other.",
"Turned down the other's offer of a job or,romantic involvement.","You just don't like each other.",
"One of you was a romantic rival.,One of you was a business rival.","One of you set the other up for a crime,they didn't commit."]

throw = ["Just themselves and even they won't go out of their way.",
"Just themselves.",
"Just themselves and a close friend.",
f"Themselves and {round(random.randint(1,6)/2)} friends.",
f"Themselves and {round(random.randint(1,10)/2)} friends.",
f"An entire gang {round((random.randint(1,10)+ 5))} people.",
"The local cops or other Lawmen.",
"A powerful gang lord or small Corporation.",
"A powerful Corporation.",
"An entire city or government or agency."]

ven = ["Avoid the scum.",
"Go into a murderous rage and try to physically rip their face off.",
"Backstab them indirectly.",
"Verbally attack them.",
"Set them up for a crime or other transgression they didn't commit.",
"Set out to murder or maim them."]

lovers =["Your lover died in an accident.",
"Your lover mysteriously vanished.",
"It just didn't work out.",
"A personal goal or vendetta came between you and your lover.",
"Your lover was kidnapped.",
"Your lover went insane or cyberpsycho.",
"Your lover committed suicide.",
"Your lover was killed in a fight.",
"A rival cut you out of the action.",
"Your lover is imprisoned or exiled."]

lg =["Get rid of a bad reputation.",
"Gain power and control.",
"Get off The Street no matter what it takes.",
"Cause pain and suffering to anyone who crosses you.",
"Live down your past life and try to forget it.",
"Hunt down those responsible for your miserable life and make them pay.",
"Get what's rightfully yours.",
"Save, if possible, anyone else involved in your background, like a lover, or family member.",
"Gain fame and recognition.",
"Become feared and respected."]


# Rockerboy Lifepath

TypeOfRboy = ["Musician",
"Slam Poet",
"Street Artist",
"Performance Artist",
"Comedian",
"Orator",
"Politico",
"Rap Artist",
"DJ",
"Idoru"]

ReasonYouLeft = ["You were a jerk and the rest of the group voted you out.",
"You got caught sleeping around with another member's mainline.",
'The rest of the group was killed in a tragic "accident."',
"The rest of the group was murdered or otherwise broken up by external enemies.",
'The group broke up over "creative differences."',
"You decided to go solo."]

TypeOfVenue = ["Alternative Cafes",
"Private Clubs",
"Seedy Dive Bars",
"Guerrilla Performances",
"Nightclubs Around the City",
"On the Data Pool"]

Gunning =["Old group member who thinks you did them dirty.",
"Rival group or artist trying to steal market share.",
"Corporate enemies who don't like your message.",
'Critic or other "influencer" trying to bring you down.',
"Older media star who feels threatened by your rising fame.",
"Romantic interest or media figure who wants revenge for personal reasons."]

# Solo life path

SoloType =["Bodyguard",
"Street Muscle for Hire",
"Corporate Enforcer who takes jobs on the side",
"Corporate or Freelance Black Ops Agent",
"Local Vigilante for Hire",
"Assassin/Hitman for Hire"]

MoralCompass = ['Always working for good, trying to take out the "bad guys."',
'Always spare the innocent (elderly, women, children, pets).',
"Will occasionally slip and do unethical or bad things, but it's rare.",
"Ruthless and profit centered; you will work for anyone, take any job for the money.",
"Willing to bend the rules (and the law) to get the job done.",
"Totally evil. You engage in illegal, unethical work all the time; in fact, you enjoy it."]

OperatingTerritory=["A Corporate Zone",
"Combat Zones",
"The whole City",
"The territory of a single Corporation",
"The territory of a particular Fixer or contact",
"Wherever the money takes you"]

SoloGunning = ["A Corporation you may have angered.",
"A boostergang you may have tackled earlier",
"Corrupt Lawmen or Lawmen who",
"mistakenly think you're guilty of something.",
"A rival Solo from another Corp.",
"A Fixer who sees you as a threat.",
"A rival Solo who sees you as their nemesis."]

# Netrunner lifepath

TypeOfNetrunner = ["Freelancer who will hack for hire.",
'Corporate "clone runner" who hacks for the Man.',
'Hacktivist interested in cracking systems and exposing bad guys.',
'Just like to crack systems for the fun of it.',
'Part of a regular team of freelancers.',
'Hack for a Media, politico, or Lawman who hires you as needed.']

PartnerIdentity = ["Freelancer who will hack for hire.",
'Corporate "clone runner" who hacks for the Man.',
'Hacktivist interested in cracking systems and exposing bad guys.',
'Just like to crack systems for the fun of it.',
'Part of a regular team of freelancers.',
'Hack for a Media, politico, or Lawman who hires you as needed.']

TypeOfWorkspace = ['There are screens everywhere.',
'It looks better in Virtuality, you swear.',
"It's a filthy bed covered in wires.",
'Corporate, modular, and utilitarian.',
"Minimalist, clean, and organized.",
"It's taken over your entire living space."]

TypeOfClients = ["Local Fixers who send you clients.",
"Local gangers who also protect your work area while you sweep for NET threats.",
'Corporate Execs who use you for "black project" work.',
'Local Solos or other combat types who use you to keep their personal systems, secure.',
'Local Nomads and Fixers who use you to keep their family systems secure.',
'You work for yourself and sell whatever data you can find on the NET.']

ProgramsOrigin = ["Dig around in old abandoned City Zones.",
"Steal them from other Netrunners you brain-burn.",
"Have a local Fixer supply programs in exchange for hack work.",
"Corporate Execs supply you with programs in exchange for your services.",
"You have backdoors into a few Corporate warehouses.",
"You hit the Night Markets and score programs whenever you can."]

NetrunnerGunning = ["You think it might be a rogue AI or a NET Ghost. Either way, it's bad news.",
"Rival Netrunners who just don't like you.",
"Corporates who want you to work for them exclusively.",
'Lawmen who consider you an illegal "black hat" and want to bust you.',
"Old clients who think you screwed them over.",
"Fixer or another client who wants your services exclusively."]

# Tech lifepath

TypeOfTech = ["Cyberware Technician",
"Vehicle Mechanic",
"Jack of All Trades",
"Small Electronics Technician",
"Weaponsmith",
"Crazy Inventor",
"Robot and Drone Mechanic",
"Heavy Machinery Mechanic",
"Scavenger",
"Nautical Mechanic"]

TechPartnerIdentity = ["Family member",
"Old friend",
"Possible romantic partner as well",
"Mentor",
"Secret partner with mob/gang connections",
"Secret partner with Corporate connections"]

TechTypeOfWorkspace = ["A mess strewn with blueprint paper.",
"Everything is color coded, but it's still a nightmare.",
"Totally digital and",
"obsessively backed up every day.",
"You design everything on your Agent.",
"You keep everything just in case you need it later.",
"Only you understand your filing system."]

TechTypeOfClients = ["Local Fixers who send you clients.",
"Local gangers who also protect your work area or home.",
'Corporate Execs who use you for "black project" work.',
"Local Solos or other combat types who use you for weapon upkeep.",
'Local Nomads and Fixers who bring you "found" tech to repair.',
"You work for yourself and sell what you invent/repair."]

SuppliesOrigin = ["Scavenge the wreckage you find in abandoned City Zones.",
"Strip gear from bodies after firefights.",
"Have a local Fixer bring you supplies in exchange for repair work.",
"Corporate Execs supply you with stuff in exchange for your services.",
"You have backdoor into a few Corporate warehouses.",
"You hit the Night Markets and score deals whenever you can."]

TechGunning = ["Combat Zone gangers who want you to work for them exclusively.",
"Rival Tech trying to steal your customers.",
"Corporates who want you to work for them exclusively.",
"Larger manufacturer trying to bring you down because your mods are a threat.",
"Old client who thinks you screwed them over.",
"Rival Tech trying to beat you out for resources and parts."]

# Medtech lifepath

MedtechType = ["Surgeon",
"General Practitioner",
"Trauma Medic",
"Psychiatrist",
"Cyberpsycho Therapist",
"Ripperdoc",
"Cryosystems Operator",
"Pharmacist",
"Bodysculptor",
"Forensic Pathologist"]

MedtechPartner = ["Trauma Team group",
"Old friend",
"Possible romantic partner as well",
"Family member",
"Secret partner with mob/gang connections",
"Secret partner with Corporate connections"]

MedTechTypeOfWorkspace = ["Sterilized daily in the morning like clockwork.",
"It's not state-of-the-art anymore, but it's",
"comfortable to you.",
"Your cryo equipment is also used to cool drinks.",
"Everything possible is single-use and stored",
"compacted until needed.",
"Not as clean as many of your patients",
"may have hoped.",
"Meticulously organized, sharpened, and sterilized."]

MedTechTypeOfClients = ["Local Fixers who send you clients.",
"Local gangers who also protect your work area or home in exchange for medical help.",
'Corporate Execs who use you for "black project" medical work.',
"Local Solos or other combat types who use you for medical help.",
"Local Nomads and Fixers who bring you wounded clients.",
"Trauma Team paramedical work."]

SuppliesOrigin = ["Scavenge stashes of medical supplies you find in abandoned City Zones.",
"Strip parts from bodies after firefights.",
"Have a local Fixer bring you supplies in exchange for medical work.",
"Corporate Execs or Trauma Team supply you with stuff in exchange for your services.",
"You have a backdoor into a few Corporate or Hospital warehouses.",
"You hit the Night Markets and score deals whenever you can."]

MediaType = ["Blogger",
"Writer (Books)",
"Videographer",
"Documentarian",
"Investigative Reporter",
"Street Scribe"]

MediaPublications = ["Monthly magazine",
"Blog",
"Mainstream vid feed",
"News channel",
'"Book" sales',
"Screamsheets"]

MediaEthics = ["Fair, honest reporting, strong ethical practices. You only report the verifiable truth.",
"Fair and honest reporting, but willing to go on hearsay and rumor if that's what it takes.",
"Will occasionally slip and do unethical things, but it's rare. You have some standards.",
"Willing to bend any rules to get the bad guys. But only the bad guys.",
"Ruthless and determined to make it big, even if it means breaking the law. You're a muckraker.",
"Totally corrupt. You take bribes, engage in illegal, unethical",
"reporting all the time. Your pen is for hire to the highest bidder."]

MediaStories = ["Political Intrigue",
"Ecological Impact",
"Celebrity News",
"Corporate Takedowns",
"Editorials",
"Propaganda"]

# Exec Lifepath

CorpoType = ["Financial",
"Media and Communications",
"Cybertech and Medical Technologies",
"Pharmaceuticals and Biotech",
"Food, Clothing, or other General Consumables",
"Energy Production",
"Personal Electronics and Robotics",
"Corporate Services",
"Consumer Services",
"Real Estate and Construction"]

CorpoDivision = ["Procurement",
"Manufacturing",
"Research and Development",
"Human Resources",
"Public Affairs/Publicity/Advertising",
"Mergers and Acquisitions"]

CorpoAlignement = ["Always working for good, fully supporting ethical practices.",
"Operates as a fair and honest business all the time.",
"Will occasionally slip and do unethical things, but it's rare.",
"Willing to bend the rules to get what it needs.",
"Ruthless and profit-centered, willing to do some bad things.",
"Totally evil. Will engage in illegal, unethical business all the time."]

CorpoBased = ["One city",
"Several cities",
"Statewide",
"National",
"International, offices in a few major cities",
"International, offices everywhere"]

CorpoGunning = ["Rival Corp in the same industry.",
"Law enforcement is watching you.",
"Local Media wants to bring you down.",
"Different divisions in your own company are feuding with each other.",
"Local government doesn't like your Corp.",
"International Corporations are eyeing you for a hostile takeover."]

CorpoBoss = ["Your Boss mentors you but watch out for their enemies.",
"Your Boss gives you a free hand and doesn't want to know what you're up to.",
"Your Boss is a micromanager who tries to meddle in your work.",
"Your Boss is a psycho whose unpredictable outbursts are offset by quiet paranoia.",
"Your Boss is cool and watches your back against rivals.",
"Your Boss is threatened by your meteoric rise and is planning to knife you."]

# Lawman Lifepath

LawmanRank = ["Guard",
"Standard Beat or Patrol",
"Criminal Investigation",
"Special Weapons and Tactics",
"Motor Patrol",
"Internal Affairs"]

LawmanJurisdiction = ["Corporate Zones",
"Standard City Patrol Zone",
"Combat Zones",
"Outer City",
"Recovery Zones",
"Open Highways"]

GroupAlignement = ["Fair, honest policing, strong ethical practices.",
"Fair and honest policing, but hard on lawbreakers.",
"Will occasionally slip and do unethical things, but it's rare.",
"Willing to bend any rules to get the bad guys.",
"Ruthless and determined to control The Street, even if it means breaking the law.",
"Totally corrupt. You take bribes, engage in illegal, and unethical business all the time."]

LawmanGunning = ["Organized Crime",
"Boostergangs",
"Police Accountability Group",
"Dirty Politicians",
"Smugglers",
"Street Criminals"]

GroupTarget = ["Organized Crime",
"Boostergangs",
"Drug Runners",
"Dirty Politicians",
"Smugglers",
"Street Crime"]

# Fixer Lifepath

TypeOfFixer = ["Broker deals between rival gangs.",
"Procure rare or atypical resources for exclusive clientele.",
"Specialize in brokering Solo or Tech services as an agent.",
"Supply a regular resource for the Night Markets, like food, medicines, or drugs.",
"Procure highly illegal resources, like street drugs or milspec weapons.",
"Supply resources for Techs and Medtechs, like parts and medical supplies.",
"Operate several successful Night Markets, although not as owner.",
"Broker use contracts for heavy machinery, military vehicles, and aircraft.",
"Broker deals as a fence for scavengers raiding Corps or Combat Zones.",
"Act as an exclusive agent for a Media, Rockerboy, or a Nomad Pack."]

FixerPartnerIdentity = ["Family member",
"Old friend",
"Possible romantic partner as well",
"Mentor",
"Secret partner with mob/gang connections",
"Secret partner with Corporate connections"]

FixerOffice = ["You don't have one. You like to keep it mobile.",
"A booth in a local bar.",
"All Data Pool messages and anonymous dead drops.",
"Spare room in a warehouse, shop, or clinic.",
"An otherwise abandoned building.",
"The lobby of a cube hotel."]

FixerTypeOfClients = ["Local Rockerboys or Medias who use you to get them gigs or contacts.",
"Local gangers who also protect your work area or home.",
'Corporate Execs who use you for "black project" procurement work.',
"Local Solos or other combat types who use you to get them jobs or contacts.",
"Local Nomads and Fixers who use you to set up transactions or deals.",
"Local politicos or Execs who depend on you for finding out information."]

FixerGunning = ["Combat Zone gangers who want you to work for them exclusively.",
"Rival Fixers trying to steal your clients.",
"Execs who want you to work for them exclusively.",
'Enemy of a former client who wants to clean up "loose ends"—like you.',
"Old client who thinks you screwed them over.",
"Rival Fixer trying to beat you out for resources and parts."]

# Nomad lifepath

NomadPackSize = ["A single extended tribe or family",
"A couple dozen members",
"Forty or fifty members",
"A hundred or more members"
"A Blood Family (hundreds of members)",
"An Affiliated Family (made of several Blood Families)"]

NomadLandOperations = ["Gogang",
"Passenger transport",
"Chautauqua/school",
"Traveling show/carnival",
"Migrant farmers",
"Cargo transport",
"Shipment protection",
"Smuggling",
"Mercenary army",
"Construction work gang"]

NomadAirOperations = ["Air piracy"
"Cargo transport"
"Passenger transport"
"Aircraft protection"
"Smuggling"
"Combat support"]

NomadSeaOperations = ["Piracy",
"Cargo transport",
"Passenger transport",
"Smuggling",
"Combat support",
"Submarine warfare"]

PlayerPackRole = ["Scout (negotiator)",
"Outrider (protection, weapons)",
"Transport pilot/driver",
"Loadmaster (large cargo mover, trucker)",
"Solo smuggler",
"Procurement (fuel, vehicles, etc.)"]

PlayerPackPhilosophy = ["Always working for good; your Pack accepts others, just wants to get along.",
"It's more like a family business. Operates as a fair and honest concern.",
"Will occasionally slip and do unethical things, but it's rare.",
"Willing to bend the rules whenever they get in the way to get what the Pack needs.",
"Ruthless and self-centered, willing to do some bad things if it will get the Pack ahead.",
"Totally evil. You rage up and down the highways,",
"killing, looting, and just terrorizing everyone."]

PlayerPackPhilosophy = ["Organized Crime",
"Boostergangs",
"Drug Runners",
"Dirty Politicians",
"Rival Packs in the same businesses",
"Dirty Cops"]

RandomMaleNames = ["Wyatt Alessandro",
"Daron Helsing",
"Loki Bucanan",
"Micah Chalet",
"Stefan Wynter",
"Tyrel Flanigan",
"Ulric Iavarone",
"Porter Markell",
"Holbrook Flanigan",
"Hawthorne Engstrom",
"Boone Flanigan",
"Random Callahan",
"Nicol Grippen",
"Xeno Wildner",
"Uruk Jann",
"Dylan Ghelfi",
"Marten Jann",
"Cory Vangelos",
"Errol Lavigne",
"Lachlan Dituri",
"Uruk Chalet",
"Darwin Jadin",
"Ivan Reade",
"Damien Maille",
"Valen Castiglione",
"Archer Malik",
"Rory Sharpey",
"Loki Vasser",
"Ewan O'Heron",
"Urien Tronstad"]
