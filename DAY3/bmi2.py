height = float(input("Enter the height in m:- "))
weight = float(input("Enter the weight in kg:- "))

body_mass_index = round(weight / height ** 2)
if body_mass_index < 18.5:
    print(f"your body mass index is  {body_mass_index} and you are underweight")
elif body_mass_index < 25:
    print(f"your body mass index is  {body_mass_index} and you have normal weight")
elif body_mass_index < 30:
     print(f"your body mass index is  {body_mass_index} and you have overweight")
elif body_mass_index < 35:
     print(f"your body mass index is  {body_mass_index} and you are obeses")
else:
     print(f"your body mass index is  {body_mass_index} and you are clinically obeses")
    
