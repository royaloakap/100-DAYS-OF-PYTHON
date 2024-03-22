import random 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
lenofpassword = int(input("num of letters:"))
def password(num):
    password = ''
    for i in range(num):
        password += random.choice(chars)
    return password
print(password(lenofpassword))###*/
###* @INFO
###* Bot Coded by Royaloakap| https://discord.gg/RoyalC2
###* @INFO
###* Please mention HRoyaloakap, when using this Code
###* @INFO
###* Telegram - https://t.me/royal_faq
###*/
