age = input("Whats your current age:-")
live_until = 90

total_living_age_left = live_until -int(age)

total_living_days_left =  int(total_living_age_left) * 365
total_living_weeks_left = int(total_living_age_left) *52
total_living_month_left = int(total_living_age_left) * 12

print(f"you have {total_living_days_left} days, {total_living_weeks_left} weeks and {total_living_month_left} months left.")