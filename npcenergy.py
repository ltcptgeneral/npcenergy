from os import system, name
import time
import csv

from anytree import Node, RenderTree

from database import database
from character import character
from enemy import enemy
from item import item

def loaddata():

    with open("data/savdata", newline = '') as csvfile:
        file_array = list(csv.reader(csvfile))
        csvfile.close()
    return file_array

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def intro(data):

    clear()
    
    print("All decent RPGs begin with the one important question: who the fuck are you? Its time for you to decide.")
    name = input("Press Enter to continue")
    clear()
    
    print("First what's your gender? Notice how PC we are by giving you a chance to create any gender you want.")
    gender = input("Gender: ")
    clear()
    
    print("Every protagonist has a name, what's your's? ") 
    name = input("Name: ")
    clear()
    
    print("Now that I have no more than a basic understanding of yourself, we immedietly procede to everyone's favorite thing: exposition!")
    clear()
    
    print("In these fable times, dangers are scarce and Heroes even scarcer. However what plagues the nations are troubles of monotony. You were born in this time, and in the meager years of childhood you have yet to escape the endless tasks given by society. The aware individuals realize that every problem has some intrinsic set of reasons. So you, being an aware individual, realize that your childhood problems began at birth. Specifically because your were born into a family of...")
    
    while True:
        print("1) declining nobility\n2) tradesmen and merchants\n3) simple footsoldiers\n4) hunters\n5) nomadic peoples\n6) criminal masterminds")
        family = input("Select from 1 - 6: ")
        if family in ["1","2","3","4","5","6", "gods"]:
            break
        else:
            print("You were never properly tought how to count apparently, as you answer was not from 1-6.")
    #clear()
    
    print({
        "1":"As the child of declining nobility, you've never real power has never been in your grasp. However you've always been expected to behave as if you were a ruler.",
        "2":"Coming from merchants and tradesman, you've had the responsibility of continuing the family trading buisness since you were born.",
        "3":"The prodigy of two simple, but honored footsoldiers, you have been trained in martial arts since 6 years of age, preparing for the time you too would be fighting on the front lines.",
        "4":"Your family has lived and died by the forest. Literally, the entire extended family lives in a ragedy thatch hut on the edge of the forest.",
        "5":"You have never known any one place as home, as the family along with the rest of the tribe keep on moving around searching for greener pastures.",
        "6":"Sabotage, smuggling, and stealing are the name of the game. And you and your family are very good at it. At the age of 13 you took over you father's criminal empire after his murder.",
        "gods":"You are the offspring of the gods. Albeit very weak gods, but gods nonetheless. You've kept sane over the years keeping in touch with the posterity of long dead friends."
        }.get(family))
    
    input("Press Enter to continue")
    clear()

    print("Of course many problems in life are not due to uncontrollable factors like the family you were born into, so naturally your psychologist would ask you to describe your childhood.")
    
    print("As a young child you were a...")

    while True:

        print("1) local lord's page\n2) engineer's apprentice\n3) warlock's assistant\n4) street urchin\n5) nomadic child")

        childhood = input("Select from 1 - 5: ")
        if childhood in ["1","2","3","4","5"]:
            break
        else:
            print("You were never properly tought how to count apparently, as you answer was not from 1-5.")
    #clear()
    
    print({
        "1":"Your first lessons as a page for the local lord was those of inequality, as you waited on those more fortunate than yourself. However in return you recieved a small stipend and a decent education.",
        "2":"As the appentice to a local engineer, you recieved a formal education in modern maths and physics. However the long hours at the desk has caused both your posture and physique to deteriorate.",
        "3":"Taken at an early age to be trained in the magical arts, you have gained basic knowledge in all things magical. However dabbling in the arts has caused both your posture and engineering intelect to deteriorate.",
        "4":"Scavenging and surviving on the streets at an early age, you have gained quite a reputation and the conbination of a lean diet and plenty of excercise has left you in decent shape. However on the strret there was a lack of schooling and books.",
        "5":"As a child of a nomadic tribe, the constant movement has left you in good shape and tribal schooling has at least given you a basic education. However being of nomadic origin leads people to look down upon you as a worse smelling than a peasant."
        }.get(childhood))

    input("Press Enter to continue")
    clear()

    print("The monotony of every day life since childhood has left you bored, and it was on this day that you decided to becom an adventurer, against the wishes of your parents. However, having never stepped out of your comfort zone before, you have no clue what it means to be an adventurer. Perhaps it would be a good idea to start by picking what kind of adventurer you wish to be. As there are many types of fish in the sea, there are many types of adventuring to me done. You decide to be a...")

    while True:
        print("1) mercenary\n2) bard\n3) student\n4) salesman\n5) craftsman\n6) hunter\n7) theif\n8) wizard")
        job = input("Select from 1 - 7: ")
        if job in ["1","2","3","4","5","6","7","8"]:
            break
        else:
            print("You were never properly tought how to count apparently, as you answer was not from 1-8.")
    #clear()

    print({
        "1":"You decide that a life of combat is right for you.",
        "2":"You decide that a life of telling stories is right for you.",
        "3":"You decide that a life of learning and academia is right for you.",
        "4":"You decide that a life of selling and trading is right for you.",
        "5":"You decide that a life of engineering and building is right for you.",
        "6":"You decide that a life spent in the woods hunting is right for you.",
        "7":"You decide that a life of theiving and trickery is right for you.",
        "8":"You decide that a life of software (magic) is right for you."
        }.get(job))

    input("Press Enter to continue")

    clear()

    print("No doubt that answering those questions has alread exceded the maximum number of interactions allwed per day, with penalty of mental and social shutdown. So from now on there will be no social interactions required. You only need to asnwer [...] when prompted.")

    input("To practice, when you see this: [...], you only need to press Enter")

    clear()

    print("With what little you had on you back and in your pockets, you set out to find meaning in life.")
    input("Press Enter to begin your journey")

    return gender, name, family, childhood, job

def createcharacter(db, character, gender, name, family, childhood, job, base_stats, attributes):

    if family == "gods":

        character.setgender(gender)
        character.setname(name)

        character.setskills(db.getmaxskills())

        character.setfamily(family)
        character.setchildhood(childhood)
        character.setjob(job)

        character.setbasestats({
            "hp":1000,
            "attk": 1000,
            "defence":1000,
            "intellect":1000
            })

        character.setattributes({
            "hp":8001,
            "attk": 8001,
            "defence":8001,
            "intellect":8001
            })

    else:

        character.setgender(gender)
        character.setname(name)

        skills = character.getskills()

        character.setfamily(family)
        character.setchildhood(childhood)
        character.setjob(job)

        for key in (db.getfamilies().get(family)):

            skills[key] += db.getfamilies().get(family).get(key)

        character.setskills(skills)

        skills = character.getskills()

        for key in (db.getchildhoods().get(childhood)):

            skills[key] += db.getchildhoods().get(childhood).get(key)

        character.setskills(skills)

        skills = character.getskills()

        for key in (db.getjobs().get(job)):

            skills[key] += db.getjobs().get(job).get(key)

        character.setskills(skills)

        character.setbasestats(base_stats)

        character.setattributes(attributes)

    return character

def charactercalcstats(character):

    for key in character.getattributes().keys():

        character.getadjustedstats()[key] = character.getattributes().get(key) + character.getbasestats().get(key)

    return character

global gamedb
global player
    
def main():

    gamedb = database()
    player = character()

    data = loaddata()

    if len(data) == 0:

        gender, name, family, childhood, job = intro(data)
        clear()
        player = createcharacter(gamedb, player, gender, name, family, childhood, job, {
            "hp":10,
            "attk": 0,
            "defence":0,
            "intellect":0
            }, {
            "hp": 0,
            "attk": 0,
            "defence": 0,
            "intellect": 0
            })

        player = charactercalcstats(player)
        player.setexp(0)

    else:

        clear()

        #player = createcharacter(gamedb, player, data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], base_stats, attributes)
        #print(str(data[0][2]))
        #print(gamedb.getfamilies().get(str(data[0][2])))
        
        player = createcharacter(gamedb, player, str(data[0][0]), str(data[0][1]), str(data[0][2]), str(data[0][3]), str(data[0][4]), {
            "hp": str(data[1][0]),
            "attk": str(data[1][1]),
            "defence": str(data[1][2]),
            "intellect": str(data[1][3])
            }, {
            "hp": str(data[2][0]),
            "attk": str(data[2][1]),
            "defence": str(data[2][2]),
            "intellect": str(data[2][3])
            })
        
        player.setexp(data[3][0])
        
    #print(player.getadjustedstats(), player.getname(), player.getgender(), player.getexp(), player.getskills())

if __name__ == "__main__":
    main()
