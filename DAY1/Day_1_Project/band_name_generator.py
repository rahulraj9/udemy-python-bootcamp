import datetime
current_time = datetime.datetime.now()
greeting ="welcome to Band Name Generator"
if current_time.hour < 12:
    print("Good Morning \n "+greeting)
elif 12 <=  current_time.hour < 18:
    print("Good Afternoon \n" +greeting)
else:
    print("Good Evening \n" +greeting)
city_name = input("Enter your city name\n")
pet_name = input("Enter you pet name\n")
print("Band name Generetring...")

print("Your Band name is :-\n")
print(city_name + pet_name)
