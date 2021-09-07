import datetime
current_time = datetime.datetime.now()
greeting ="welcome to Love calculator"
if current_time.hour < 12:
    print("Good Morning \n "+greeting)
elif 12 <=  current_time.hour < 18:
    print("Good Afternoon \n" +greeting)
else:
    print("Good Evening \n" +greeting)

lover_name1 = input("what is your name:----").lower()
lover_name2 = input("\nwhat is their name:----").lower()

couplename = lover_name1+lover_name2

# count True

total_count_of_true = couplename.count("t") + couplename.count("r") + couplename.count("u") + couplename.count("e")
total_count_of_love = couplename.count("l") + couplename.count("o") + couplename.count("v") + couplename.count("e")

total_true_love_score = str(total_count_of_true)+ str(total_count_of_love)



if int(total_true_love_score) < 10 and int(total_true_love_score) > 90:
    print(f"your score is {total_true_love_score}, you go together like coke and mentos.")
elif int(total_true_love_score) > 40 and int(total_true_love_score) < 50:
    print(f"Your score is {total_true_love_score}, you are alright together.")
else:
    print(f"Your score is {total_true_love_score}")