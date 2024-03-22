#Python program to get the largest number from a list.
import functools as fun
print("WELCOME...TO FIND THE MAX NO. IN LIST:::")
l=list(map(int,input("ENTER THE ELEMENT OF LIST SPACE SEPARATED: ").split()))
ele=fun.reduce(lambda a,b:a if a>b else b,l)
print("MAXIMUM NUM IS :",ele)###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
