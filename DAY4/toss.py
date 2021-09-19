import random

random_number_integer  =  random.randint(0,1)
HEADS = 1
TAILS = 0

print(random_number_integer)

toss_input= input("what you want 'HEADS OR TAILS'\n").upper()

if random_number_integer == HEADS:
    print("coin is on head")
    if toss_input == "HEADS":
        print("HEADS\nyou won the toss")
    else:
        print("you loss the toss")

else:
    print("coin is Tails")
    if toss_input == "Tails":
        print("Heads\nyou won the toss")
    else:
        print("you loss the toss")