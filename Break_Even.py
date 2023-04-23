#BreakEven.py - A simple program to determine how to set the price to resell your Sounders Season tickets to break even.

#Ask the user how much they paid for their season ticket

season_ticket = eval(input ("How much did  you pay for your season ticket package?"))

#Ask how many games there are in the season ticket package

total_games = eval(input ("How many games are included in your season ticket package?"))

#Ask how many games the user plans to go to

games_attended = eval(input ("Of the total games included, how many games to plan to  attend?"))

#Subtract games_attended from total_games to determine the difference in games to  sell tickets for

remaining_games  = total_games - games_attended

#Divide the price of the package by the number of games

ask_for  = season_ticket /  remaining_games

#Print how much each ticket should cost to get their money back

print ("In order to  break even on your season ticket package, you will need to sell each ticket for $",round(ask_for, 2), ".")
