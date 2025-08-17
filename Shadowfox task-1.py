
# PYTHON ASSIGNMENT



print("\n--- 1. VARIABLES ---")


pi = 22 / 7
print("Value of pi:", pi)
print("Data type:", type(pi))


print("NOTE: 'for = 4' gives SyntaxError because 'for' is a reserved keyword.")
P = 1000
R = 5
T = 3
SI = (P * R * T) / 100
print("Simple Interest:", SI)
print("\n--- 2. NUMBERS ---")


def format_example(num, fmt):
    return format(num, fmt)

print("145 in octal:", format_example(145, 'o'))


r = 84
pi = 3.14
area = pi * (r ** 2)
print("Pond Area:", area)
water = int(area * 1.4)
print("Total water in pond (liters):", water)


distance = 490
time_min = 7
time_sec = time_min * 60
speed = int(distance / time_sec)
print("Speed:", speed, "m/s")

print("\n--- 3. LIST ---")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]


print("Members:", len(justice_league))


justice_league.extend(["Batgirl", "Nightwing"])
print("After adding:", justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Leader update:", justice_league)

justice_league.insert(justice_league.index("Flash"), "Superman")
print("Separated:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Team:", justice_league)

justice_league.sort()
print("Sorted:", justice_league)
print("New Leader:", justice_league[0])


print("\n--- 4. IF CONDITION ---")
h = 1.75
w = 70
bmi = w / (h ** 2)
print("BMI:", bmi)
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")


Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = "Abu Dhabi"
if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")


city1, city2 = "Mumbai", "Chennai"

def find_country(city):
    if city in Australia: return "Australia"
    if city in UAE: return "UAE"
    if city in India: return "India"
    return None

c1, c2 = find_country(city1), find_country(city2)
if c1 and c2 and c1 == c2:
    print("Both cities are in", c1)
else:
    print("They don't belong to the same country")



print("\n--- 5. FOR LOOP ---")
import random


rolls = [random.randint(1, 6) for _ in range(20)]
print("Rolls:", rolls)
print("Count of 6:", rolls.count(6))
print("Count of 1:", rolls.count(1))
consecutive_sixes = sum(1 for i in range(len(rolls)-1) if rolls[i] == rolls[i+1] == 6)
print("Two 6s in a row:", consecutive_sixes)


total = 0
for i in range(10):
    total += 10
    print(f"You have done {total} jumping jacks")
    if total >= 100:
        print("Congratulations! You completed the workout")
        break

    print(f"{100-total} jumping jacks remaining")


print("\n--- 6. DICTIONARY ---")


friends = ["Aditya", "Neha", "Rohit", "Sanjay", "Pooja"]
friends_info = [(name, len(name)) for name in friends]
print("Friends info:", friends_info)

your_expenses = {"Hotel": 1200,"Food": 800,"Transportation": 500,"Attractions": 300,"Miscellaneous": 200}
partner_expenses = {"Hotel": 1000,"Food": 900,"Transportation": 600,"Attractions": 400,"Miscellaneous": 150}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())
print("Your total:", your_total)
print("Partner total:", partner_total)
print("Who spent more:", "You" if your_total > partner_total else "Partner")

diffs = {k: abs(your_expenses[k]-partner_expenses[k]) for k in your_expenses}
max_cat = max(diffs, key=diffs.get)
print("Biggest difference in:", max_cat, "=", diffs[max_cat])



print("\n--- 7. FILE HANDLING ---")
import csv


students = [
    {"Name": "Amit", "RollNo": "1", "Math": "80", "Science": "75", "English": "90"},
    {"Name": "Neha", "RollNo": "2", "Math": "60", "Science": "85", "English": "70"},
]

for student in students:
    marks = [int(student[subject]) for subject in student if subject not in ["Name", "RollNo"]]
    student["Total"] = sum(marks)
    student["Average"] = student["Total"] / len(marks)


with open("student_with_totals.csv", "w", newline='') as f:
    fieldnames = students[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
print("Student data with totals saved to student_with_totals.csv")


print("\n--- 8. CLASSES & OBJECTS ---")

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        return f"{self.name}: {self.super_power}, Weapon: {self.weapon}"

    def is_leader(self):
        return self.leader

super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True),
    Avenger("Iron Man", 45, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    print(hero.get_info(), "| Leader:", hero.is_leader())



print("\n--- 9. INHERITANCE ---")

class MobilePhone:
    def __init__(self, screen, network, dual_sim, front, rear, ram, storage):
        self.screenType = screen
        self.networkType = network
        self.dualSim = dual_sim
        self.frontCamera = front
        self.rearCamera = rear
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")
    def receive_call(self):
        print("Incoming call...")
    def take_picture(self):
        print(f"Taking picture with {self.rearCamera} rear camera")

class Apple(MobilePhone):
    def __init__(self, model, *args):
        super().__init__(*args)
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model, *args):
        super().__init__(*args)
        self.model = model


iphone = Apple("iPhone 14", "Touch Screen", "5G", False, "12MP", "48MP", "6GB", "128GB")
samsung = Samsung("Galaxy S22", "Touch Screen", "5G", True, "16MP", "64MP", "8GB", "256GB")

iphone.make_call("1234567890")
samsung.take_picture()



