import random
def code():
  print('Welcome to rock paper scissor game.\nPlease press run to restart.')
  op1 = 'rock' 
  op2 = 'paper'
  op3 = 'scissor'
  option = [op1,op2,op3]
  player_option = ["1" , "2" , "3"]
  choice = int(input("Please select your choice: press '1' for Rock , '2' for Paper , '3' for scissor\nPlease type out your choice correctly: \n"))
  bot = random.choice(option)
  def outcome():
    if choice == op1 and bot == op2 or choice == op2 and bot == op3 or choice == op3 and bot == op1:
      print("\nLMAO,YOU LOST TO A BOT IN ROCK PAPER SCISSOR!?\n\nHOLY SKILL ISSUE!!!!!!!!\n")
      code()
    elif choice == op1 and bot == op3 or choice == op2 and bot == op1 or choice == op3 and bot == op2:
      print("\nGood job!! You win!\n \nYou may now have dinner cuz you didn't fail.\n")
      code()
    elif choice == bot:
      print("\nTIE!!!\n")
      code()
  if choice == 1:
    choice = op1
    print("You picked: " + op1)
    print(" ")
    print("Computor picked: " + bot)
  elif choice == 2:
    choice = op2
    print("You picked: " + op2)
    print(" ")
    print("Computor picked: " + bot)
  elif choice == 3:
    choice = op3
    print("You picked: " + op3)
    print(" ")
    print("Computor picked: " + bot)
  else:
    print("Not an option :( ")
    code()
  outcome()
  
import random
print('Welcome to rock paper scissor game.\nPlease press run to restart.')
op1 = 'rock' 
op2 = 'paper'
op3 = 'scissor'
option = [op1,op2,op3]
player_option = ["1" , "2" , "3"]
choice = int(input("Please select your choice: press '1' for Rock , '2' for Paper , '3' for scissor\nPlease type out your choice correctly: \n"))
bot = random.choice(option)
def outcome():
  if choice == op1 and bot == op2 or choice == op2 and bot == op3 or choice == op3 and bot == op1:
    print("\nLMAO,YOU LOST TO A BOT IN ROCK PAPER SCISSOR!?\n\nHOLY SKILL ISSUE!!!!!!!!\n")
    code()
  elif choice == op1 and bot == op3 or choice == op2 and bot == op1 or choice == op3 and bot == op2:
    print("\nGood job!! You win!\n \nYou may now have dinner cuz you didn't fail.\n")
    code()
  elif choice == bot:
    print("\nTIE!!!\n")
    code()
if choice == 1:
    choice = op1
    print("You picked: " + op1)
    print(" ")
    print("Computor picked: " + bot)
elif choice == 2:
  choice = op2
  print("You picked: " + op2)
  print(" ")
  print("Computor picked: " + bot)
elif choice == 3:
  choice = op3
  print("You picked: " + op3)
  print(" ")
  print("Computor picked: " + bot)
else:
  print("Not an option :( ")
  code()
outcome()
