#Python program to get the smallest number from a list
import functools as fun
print("TO FIND THE SMALLEST NUM IN LIST:::")
lst=list(map(int,input("ENTER THE ELEMENTS SPACE SEPARATED: ").split()))
ele=fun.reduce(lambda a,b:a if b>a else b,lst)
print("SMALLEST NUM IS:",ele)###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
