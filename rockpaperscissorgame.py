import random
op1 = "rock"
op2 = "paper"
op3 = "scissor"
options = [op1,op2,op3]
botoption = [op1,op2,op3]
print("Welcome to Rock Paper Scissor Game!")
def code():
  while True:
    bot = random.choice(botoption)
    option = input("\nPlease enter your choice.\n\n press 1 for rock\n\n press 2 for paper\n\n press 3 for scissor\n\n press 4 to exit...\n\nEnter your choice: \n")
    if not option.isdigit():
      print("Not an option :(")
      code()
    choice = option
    choice = int(choice)
    if choice == 1:
      choice = op1
    elif choice == 2:
      choice = op2
    elif choice == 3:
      choice = op3
    if choice == op1 and bot == op3 or choice == op2 and bot == op1 or choice == op3 and bot == op2:
        print("\nYOU PICKED: " + choice+"\n")
        print("\nBOT PICKED: " + bot)
        print("You win!")
        code()
    elif choice == op1 and bot == op2 or choice == op2 and bot == op3 or choice == op3 and bot == op1:
        print("YOU PICKED: " + choice+"\n")
        print("\nBOT PICKED: " + bot)
        print("LMAO, YOU LOST TO A BOT !? LITTERALLY HOW? YOU SUCK AT THE OLDEST GAME IN THE BOOK!!")
        code()
    elif choice == bot:
      print("YOU PICKED: " + choice+"\n")
      print("BOT PICKED: " + bot)
      print("TIE!!!")
code()
