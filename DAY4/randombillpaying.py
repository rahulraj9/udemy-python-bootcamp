import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total_group_size = len(names)
randaom_number_interger = random.randint(0,total_group_size-1)
print(f"{names[randaom_number_interger]} is going to buy the meal today ")
