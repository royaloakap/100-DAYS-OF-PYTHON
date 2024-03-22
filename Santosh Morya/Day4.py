import random
choices = ['rock','paper','scissor']
User = input("Choose among rock,paper and scissor:- ")
print("you entered: ",User)
if User in choices:
    choices.remove(User)
    computer =random.choice(choices)
    if((User == 'rock' and computer == 'scissor' ) or (User == 'paper' and computer == 'rock') or (User == 'scissor' and computer == 'paper')):
        print("You won")
    else:
        print("Computer won")    
else:
    print("Enter the valid input")
###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
