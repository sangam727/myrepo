import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = [rock,paper,scissors]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for for Paper and 2 for Scissors.\n"))

if user_choose >=3 or user_choose < 0:
  print("you type invalid number, you lose!")
else:
  print(choice[user_choose])
  print("Computer chose:\n")
  computer_chose = random.randint(0,2)
  print(choice[computer_chose])
  
  if user_choose == 0 and computer_chose == 2:
    print("You won!")
  elif computer_chose == 0 and user_choose ==2:
    print("You lose.")
  elif user_choose > computer_chose:
    print("You win!")
  elif computer_chose > user_choose:
    print("You lose.")
  elif user_choose == computer_chose:
    print("It's draw.")