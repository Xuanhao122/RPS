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

player = int(input("Type 0 for rock, 1 for paper, and 2 for scissors."))
RPS = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print(RPS[player])

print(f"Computer chose:\n{RPS[computer_choice]}")

decision = ["Draw", "You Lose", "You Win"]
decision_2 = ["You Win","Draw", "You Lose"]
decision_3 = ["You Lose", "You Win", "Draw"]

decision_all = [decision, decision_2, decision_3]

print(decision_all[player][computer_choice])