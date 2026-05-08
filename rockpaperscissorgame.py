import random
import sys

#introduction:
print('Welcome to rock paper scissor game.\nPlease press run to restart.')


# options:
op1 = 'rock'
op2 = 'paper'
op3 = 'scissor'
option = [op1,op2,op3]


# choices:
choice = input(f'Please select your choice: {op1} , {op2} , {op3}\nPlease type out your choice correctly: \n').strip().lower()
bot = random.choice(option)
print(bot)
if choice == bot:
  print("TIE!!!")
elif choice == op1 and bot == op3 or choice == op2 and bot == op1 or choice == op3 and bot == op2:
  print("Good job!! You win! \nYou may now have dinner cuz you didn't fail.\n")
elif choice not in option:
  print("Not an option! :( \nPlease press run to restart\n")
  sys.exit()
else:
  print("LMAO,YOU LOST TO A BOT IN ROCK PAPER SCISSOR!?\nHOLY SKILL ISSUE!!!!!!!!\n")
