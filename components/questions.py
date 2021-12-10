from components import gameVars
from time import sleep

def Questions():
        #question 1
    while gameVars.question_Loop_1 is True:
        print("---------------------------------------")
        print("Question 1: Do you use a weapon to fight? (ex. shield, repulsors, sword, esc)")
        sleep(1)
        gameVars.answer_1 = input("(yes/no):   ")
    
        sleep (0.5)
    
        if gameVars.answer_1 in gameVars.yes_no:
            gameVars.question_Loop_1 = False
    
        else:
            print ("Your response was incorrect, please try again.")
            sleep (0.5)
        
    #question 2
    while gameVars.question_Loop_2 is True:
        print("---------------------------------------")
        print("Question 2: Is your outfit primarily red? (Excluding Capes)")
        sleep(1)
        gameVars.answer_2 = input("(yes/no):   ")
    
        sleep (0.5)
    
        if gameVars.answer_2 in gameVars.yes_no:
            gameVars.question_Loop_2 = False
    
        else:
            print ("Your response was incorrect, please try again.")
            sleep (0.5)
        
    #question 3
    while gameVars.question_Loop_3 is True:
        print("---------------------------------------")
        print("Question 3: Do you often break the fourth wall?")
        sleep(1)
        gameVars.answer_3 = input("(yes/no):   ")

        sleep(0.5)
        
        if gameVars.answer_3 in gameVars.yes_no:
            gameVars.question_Loop_3 = False
        
        else:
            print ("Your response was incorrect, please try again.")
            sleep (0.5)
    
    #question 4
    while gameVars.question_Loop_4 is True:
        print("---------------------------------------")
        print("Question 4: Do you care if you get hurt?")
        sleep(1)
        gameVars.answer_4 = input("(yes/no):   ")
        
        if gameVars.answer_4 in gameVars.yes_no:
            gameVars.question_Loop_4 = False
        else:
            print ("Your response was incorrect, please try again.")
            sleep(0.5)
            
    #question 5
    while gameVars.question_Loop_5 is True:
        print("---------------------------------------")
        print("Question 5: Do you hate masks?")
        sleep(1)
        gameVars.answer_5 = input("(yes/no):   ")
        sleep(0.5)

        if gameVars.answer_5 in gameVars.yes_no:
            gameVars.question_Loop_5 = False

        else:
            print ("your responce was incorrect, please try again.")
            sleep (0.5)
        
    #question 6
    while gameVars.question_Loop_6 is True:
        print("---------------------------------------")
        print("Question 6: Can you scale tall structures without any asistance from tech or other means?")
        sleep(1)
        gameVars.answer_6 = input("(yes/no):   ")
        sleep(0.5)

        if gameVars.answer_6 in gameVars.yes_no:
            gameVars.question_Loop_6 = False

        else:
            print ("your responce was incorrect, please try again.")
            sleep (0.5)
        
    #question 7
    while gameVars.question_Loop_7 is True:
        print("---------------------------------------")
        print("Question 7: Do you love alcohol?")
        sleep(1)
        gameVars.answer_7 = input("(yes/no):   ")
        sleep(0.5)

        if gameVars.answer_7 in gameVars.yes_no:
            gameVars.question_Loop_7 = False

        else:
            print ("your responce was incorrect, please try again.")
            sleep (0.5)
        
    #question 8
    while gameVars.question_Loop_8 is True:
        print("---------------------------------------")
        print("Question 8: Do you at all use tech to enhance your skills/abilities?")
        sleep(1)
        gameVars.answer_8 = input("(yes/no):   ")
        sleep(0.5)

        if gameVars.answer_8 in gameVars.yes_no:
            gameVars.question_Loop_8 = False

        else:
            print ("your responce was incorrect, please try again.")
            sleep (0.5)
        
    #question 9
    while gameVars.question_Loop_9 is True:
        print("---------------------------------------")
        print("Question 9: Are you extreamly physicaly strong? (able to lift very heavy things with ease)")
        sleep(1)
        gameVars.answer_9 = input("(yes/no):   ")
        sleep(0.5)

        if gameVars.answer_9 in gameVars.yes_no:
            gameVars.question_Loop_9 = False

        else:
            print ("your responce was incorrect, please try again.")
            sleep (0.5)