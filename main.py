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
import random


gameinput= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp_inp = random.randint(0,2)

if gameinput >=3 or gameinput <0:
  print("You have entered the wrong digit, you Lose!")

if gameinput == 0 and comp_inp==0:
  print(rock)
  print("computer choose\nRock")
  print(rock)
  print("It's a draw")
if gameinput == 1 and comp_inp==0:
  print(paper)
  print("computer choose\nRock")
  print(rock)
  print("you won")
if gameinput ==2 and comp_inp==0:
  print(scissors)
  print("computer choose\nRock")
  print(rock)
  print("you Lost")
elif  gameinput == 0 and comp_inp==1:
  print(rock)
  print("computer choose\nPaper")
  print(paper)
  print("You lose")
elif  gameinput == 1 and comp_inp==1:
  print(paper)
  print("computer choose\nPaper")
  print(paper)
  print("Draw")
elif  gameinput == 2 and comp_inp==1:
  print(scissors)
  print("computer choose\nPaper")
  print(paper)
  print("Draw")
elif  gameinput == 0 and comp_inp==2:
  print(rock)
  print("computer choose\nScissor")
  print(scissors)
  print("You won")
elif  gameinput == 1 and comp_inp==2:
  print(paper)
  print("computer choose\nScissor")
  print(scissors)
  print("You Lost")
elif  gameinput == 2 and comp_inp==2:
  print(scissors)
  print("computer choose\nScissor")
  print(scissors)
  print("Draw")

