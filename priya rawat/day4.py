# ROCK PAPER SCISSSORS GAME 
import random
moves =['rock','paper','scissors']
cmove = random.choice(moves)
pmove = input("What is your move : rock, paper, scissors :")
moves.remove(pmove)
print("computer move", cmove)
if pmove == 'rock' and cmove == 'scissors' :
    print("You win ")
elif pmove =='paper' and cmove == 'rock' :
    print("you win ")
elif pmove == 'scissors' and cmove == 'paper' :
    print("you won")
else:
    print("The computer won. Better luck next time")

     ###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
