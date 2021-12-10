from components import gameVars

#questions for spiderman: 4 - complete 
#questions for Deadpool: 4 - complete
#questions for thor: 2

#3 of the questions relate to 2 of the characters at the same time

def points_count():
    #question 1--------------------------------------------------
    if gameVars.answer_1 in gameVars.yes:
        gameVars.Thor = gameVars.Thor + 1
        gameVars.Deadpool = gameVars.Deadpool + 1
        
    elif gameVars.answer_1 in gameVars.no:
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        
    #question 2--------------------------------------------------
    if gameVars.answer_2 in gameVars.yes:
        gameVars.Deadpool = gameVars.Deadpool + 1
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        
    elif gameVars.answer_2 in gameVars.no:
        gameVars.Thor = gameVars.Thor + 1
        
    #question 3--------------------------------------------------
    if gameVars.answer_3 in gameVars.yes:
        gameVars.Deadpool = gameVars.Deadpool + 1
    
    elif gameVars.answer_3 in gameVars.no:
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        gameVars.Thor = gameVars.Thor + 1
        
    #question 4--------------------------------------------------
    if gameVars.answer_4 in gameVars.yes:
        gameVars.Deadpool = gameVars.Deadpool + 1
        
    elif gameVars.answer_4 in gameVars.no:
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        gameVars.Thor = gameVars.Thor + 1
        
    #question 5--------------------------------------------------
    if gameVars.answer_5 in gameVars.yes:
        gameVars.Thor = gameVars.Thor + 1

    elif gameVars.answer_5 in gameVars.no:
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        gameVars.Deadpool = gameVars.Deadpool + 1

    #question 6--------------------------------------------------
    if gameVars.answer_6 in gameVars.yes:
        gameVars.Spider_Man = gameVars.Spider_Man + 1

    elif gameVars.answer_6 in gameVars.no:
        gameVars.Thor = gameVars.Thor + 1
        gameVars.Deadpool = gameVars.Deadpool + 1

    #question 7--------------------------------------------------
    if gameVars.answer_7 in gameVars.yes:
        gameVars.Thor = gameVars.Thor + 1

    elif gameVars.answer_7 in gameVars.no:
        gameVars.Spider_Man = gameVars.Spider_Man + 1
        gameVars.Deadpool = gameVars.Deadpool + 1

    #question 8--------------------------------------------------
    if gameVars.answer_8 in gameVars.yes:
        gameVars.Spider_Man = gameVars.Spider_Man + 1

    elif gameVars.answer_8 in gameVars.no:
        gameVars.Thor = gameVars.Thor + 1
        gameVars.Deadpool = gameVars.Deadpool + 1

    #question 9--------------------------------------------------
    if gameVars.answer_9 in gameVars.yes:
        gameVars.Thor = gameVars.Thor + 1
        gameVars.Spider_Man = gameVars.Spider_Man + 1

    elif gameVars.answer_9 in gameVars.no:
        gameVars.Deadpool = gameVars.Deadpool + 1
