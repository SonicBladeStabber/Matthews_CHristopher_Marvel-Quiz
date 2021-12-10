from components import gameVars
from time import sleep



def Guess():
    while gameVars.confirm not in gameVars.yes_no:
        
        if gameVars.Thor > gameVars.Spider_Man and gameVars.Deadpool:
            print("---------------------------------------")
            print ("Are you Thor?")
            gameVars.confirm = input("(yes/no):   ")
        elif gameVars.Spider_Man > gameVars.Deadpool and gameVars.Thor:
            print("---------------------------------------")
            print ("Are you Spider Man?")
            gameVars.confirm = input("(yes/no):   ")
        elif gameVars.Deadpool > gameVars.Thor and gameVars.Spider_Man:
            print("---------------------------------------")
            print ("Are you Deadpool?")
            gameVars.confirm = input("(yes/no):   ")
            
        elif gameVars.Thor == gameVars.Deadpool or gameVars.Spider_Man:
            print("--------------------------------------------------")
            print("One or more options are available.")
            print("Did you even try to answer the questions properly?")
            break
        elif gameVars.Deadpool == gameVars.Thor or gameVars.Spider_Man:
            print("--------------------------------------------------")
            print("One or more options are available.")
            print("Did you even try to answer the questions properly?")
            break
        elif gameVars.Spider_Man == gameVars.Deadpool or gameVars.Thor:
            print("--------------------------------------------------")
            print("One or more options are available.")
            print("Did you even try to answer the questions properly?")
            break
            
            
    if gameVars.confirm in gameVars.yes:
        print("I win!")
    elif gameVars.confirm in gameVars.no:
        print("either your wrong / don't know the character /or the character you tried to get isn't here.")

def Endverse():
    while gameVars.Repeat not in gameVars.yes_no or gameVars.Repeat in gameVars.yes:
        print("---------------------------------------")
        print("want to go again?")
        gameVars.Repeat = input("(yes/no?):   ")
    
        if gameVars.Repeat in gameVars.no:
            print("goodbye")
            sleep(2)
            exit()
        
        elif gameVars.Repeat in gameVars.yes:
            gameVars.answer_1 = "empty"
            gameVars.answer_2 = "empty"
            gameVars.answer_3 = "empty"
            gameVars.answer_4 = "empty"
            gameVars.answer_5 = "empty"
            gameVars.answer_6 = "empty"
            gameVars.answer_7 = "empty"
            gameVars.answer_8 = "empty"
            gameVars.answer_9 = "empty"
            
            gameVars.question_Loop_1 = True
            gameVars.question_Loop_2 = True
            gameVars.question_Loop_3 = True
            gameVars.question_Loop_4 = True
            gameVars.question_Loop_5 = True
            gameVars.question_Loop_6 = True
            gameVars.question_Loop_7 = True
            gameVars.question_Loop_8 = True
            gameVars.question_Loop_9 = True
            
            gameVars.Thor = 0
            gameVars.Deadpool = 0
            gameVars.Spider_Man = 0
            
            print ("just enter 'exit' in any of the questions to stop playing.")
            
            sleep(3)
            break
        
        elif gameVars.Repeat not in gameVars.yes_no:
            print ("Your response was incorrect, please try again.")
            sleep (0.5)