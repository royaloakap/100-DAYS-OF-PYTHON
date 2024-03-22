#ROCK_PAPER_SCISSORS
import random
tools=['rock','paper','scissors']
player=input("Choose one of the tools:")
print(player)
computer=random.choice(tools)
print(computer)
if computer=='rock':
    if player=='paper':
        print("YOU WON...")
    else:
        print("YOU LOST...BETTER LUCK NEXT TIME")
elif computer=='paper':
    if player=='scissors':
        print("YOU WON...")
    else:
        print("YOU LOST...BETTER LUCK NEXT TIME")
elif computer=='scissors':
    if player=='rock':
        print("YOU WON...")
    else:
        print("YOU LOST...BETTER LUCK NEXT TIME")
###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
