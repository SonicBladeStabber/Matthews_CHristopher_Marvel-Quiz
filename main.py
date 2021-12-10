from components import gameVars, points, guess, questions
from time import sleep

print("The Characters that the questions referre to are:")
print("Thor")
print("Deadpool")
print("Spider Man")
print("-------------------------------------")
sleep(4)

#main sequence loop
#______________________________________________________________
while gameVars.Repeat in gameVars.yes:

    questions.Questions()    
    
    points.points_count()
    
    sleep(2)
    
    guess.Guess()
    
    
        
    sleep(4)
    
    guess.Endverse()
