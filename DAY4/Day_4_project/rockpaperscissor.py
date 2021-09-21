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

print(f"{rock}{paper}{scissors}")


computer_choice = random.randint(1,3)
print(computer_choice)
if computer_choice == 1:
    computer_choice_name = "Rock"
elif computer_choice  == 2:
    computer_choice_name = "Paper"
else:
    computer_choice_name = "Scissor"
print(f"computer choice is {computer_choice_name}")


gamer_choice = int(input("Enter choice\n1:Rock\n2:paper\n3:Scissor\n"))
if gamer_choice == 1:
    gamer_choice_name = "Rock"
elif gamer_choice == 2:
    gamer_choice_name = "Paper"
else:
    gamer_choice_name = "Scissor"
print(f"user choice is {gamer_choice_name}\nnow its couputer turn...")

if gamer_choice == 1 and computer_choice == 1 or gamer_choice == 2 and computer_choice == 2 or gamer_choice == 3 and computer_choice == 3:
    print("Draw")

elif gamer_choice == 1 and computer_choice == 2 or gamer_choice == 2 and computer_choice == 3 or gamer_choice == 3 and computer_choice == 1:
    print("computer win")

else:
    print("You win")

