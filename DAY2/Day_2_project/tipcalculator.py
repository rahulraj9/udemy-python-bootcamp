import datetime
current_time = datetime.datetime.now()
greeting ="welcome to tip calculator"
if current_time.hour < 12:
    print("Good Morning \n "+greeting)
elif 12 <=  current_time.hour < 18:
    print("Good Afternoon \n" +greeting)
else:
    print("Good Evening \n" +greeting)

total_bill = input("what was the total bill?\n$")
tip_amount = input("what percent tip would you like to give?\n 10, 12 or 15?\n")
split_bill = input("How many prople to split the bill?\n")

print(f"${total_bill} is your total bill and you give {tip_amount}% tip amount")
total_amount = int(tip_amount) / 100 *float(total_bill) + float(total_bill)
pay_per_person =  total_amount // int(split_bill)

print(f"each person should pay: ${pay_per_person}")

