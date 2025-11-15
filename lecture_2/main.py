
def generate_profile(age):
    if 0<=age<=12:
        a="Child"
        return a
    elif 13<=age<=19:
        a="Teenager"
        return a
    elif age>=20:
        a="Adult"
        return a
    else:
        err = "your age must be >=0"
while True:
    user_name = input("Enter your name: ")
    if user_name.strip() and not user_name.isdigit():
        break
    else:
        print("Name must be non-empty and not numeric\n")


while True:
    print ("enter your birth year")
    
    try:
        birth_year_str = int(input())
        if 1900 <= birth_year_str <= 2025:
            break
        else:
            print("Year must be between 1900 and 2025\n")
        break
        
    except ValueError:
        print ("year must be int\n")    

current_age = 2025 - birth_year_str

hobbies=[]

while True:
    print("Enter your favorite hobby or type 'stop' to finish")
    user_input = input()
    if user_input == "stop":
        break
    else:
        hobbies.append(user_input)
        

life_stage=generate_profile(current_age)
joined_hobbies = f"""
-""".join(hobbies)
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
Life Stage:{user_profile.get('stage')}""")

if len(hobbies)>0:
    print(f"""Favotite Hobbies({len(hobbies)})
-{user_profile.get('hobbies')}
---""")
else:
    print(f"""Favotite Hobbies({len(hobbies)})
You didn't mention any hobbies
---""")