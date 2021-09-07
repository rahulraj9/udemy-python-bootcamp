height = input("Enter the height in m:- ")
weight = input("Enter the weight in kg:- ")

body_mass_index = int(weight) / float(height)**2

print("Your BMI is :- ", int(body_mass_index))