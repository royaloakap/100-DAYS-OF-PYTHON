import random
choice = input("Choose any one between Rock - Paper - Scissor ")
game = ['Rock','Paper','Scissor']
if choice not in game:
    print("Please Enter the correct choice")
else:
    game.remove(choice)
    a = random.choice(game)
    if (choice=='Rock' and a =='Paper') or (choice=='Paper' and a =='Rock'):
        print("Paper wills")
    elif (choice=='Rock' and a =='Scissor') or (choice=='Scissor' and a =='Rock'):
        print("Rock wills")
    elif (choice=='Paper' and a =='Scissor')or (choice=='Scissor' and a =='Paper'):
        print("Scissor wills")###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
