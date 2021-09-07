import datetime
current_time = datetime.datetime.now()
greeting ="welcome to BAND PIZZA CENTER"
if current_time.hour < 12:
    print("Good Morning \n "+greeting)
elif 12 <=  current_time.hour < 18:
    print("Good Afternoon \n" +greeting)
else:
    print("Good Evening \n" +greeting)

pizza_size = input("what size you want to take ?\ns for small\nm for medium\nl for large:----")
add_pepperoni = input("Do you want pepperoni:----")
extra_cheese =input("Do you want extra cheese:----")
bill =0
if pizza_size == 's' or pizza_size == 'S':
   bill += 15
elif pizza_size == 'm' or pizza_size == 'M':
   bill += 20
else:
   bill += 25

if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if pizza_size == 's' or pizza_size == 'S':
        bill += 2
    else :
        bill += 3
if extra_cheese == 'y' or extra_cheese == 'Y' :
    bill += 1
print("******************************")
print(f"your final bill is {bill}")
print("******************************")


