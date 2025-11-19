
def generate_profile(age):
    if 0<=age<=12:
        
        return "Child"
    elif 13<=age<=19:
        
        return "Teenager"
    elif age>=20:
        
        return "Adult"
    

user_name = input("Enter your name: ")
    

while True:
    
    birth_year_str = int(input("Enter your birth year: "))
    if birth_year_str <= 2025:
        break
    else:
        print("Year must be between 1900 and 2025\n")
        break
        
    
current_age = 2025 - birth_year_str

hobbies=[]

while True:
    
    user_input = input("Enter your favorite hobby or type 'stop' to finish: ")
    if user_input == "stop":
        break
    else:
        hobbies.append(user_input)
        

life_stage=generate_profile(current_age)
joined_hobbies = f"""
- """.join(hobbies)
user_profile={
    'name':user_name,
    'age':current_age,
    'stage':life_stage,
    'hobbies':joined_hobbies
}

print (f"""
---
Profile Summary:
Name: {user_profile.get('name')}
Age: {user_profile.get('age')}
Life Stage: {user_profile.get('stage')}""")

if len(hobbies)>0:
    print(f"""Favotite Hobbies ({len(hobbies)}):
- {user_profile.get('hobbies')}
---""")
else:
    print(f"""Favotite Hobbies({len(hobbies)})
You didn't mention any hobbies
---""")