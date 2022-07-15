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
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_input = random.randint(0,2)
if player_input == 0:
  print(rock)
  if cpu_input == 0:
    game_status = "You draw"
  elif cpu_input == 1:
    game_status = "You lose"
  else:
    game_status = "You win"
elif player_input == 1:
  print(paper)
  if cpu_input == 0:
    game_status = "You win"
  elif cpu_input == 1:
    game_status = "You draw"
  else:
    game_status = "You lose"
else:
  print(scissors)
  if cpu_input == 0:
    game_status = "You lose"
  elif cpu_input == 1:
    game_status = "You win"
  else:
    game_status = "You draw"
print("Computer chose:")
if cpu_input == 0:
  print(rock)
elif cpu_input == 1:
  print(paper)
else:
  print(scissors)
print(game_status)