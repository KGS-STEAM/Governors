import random
from sense_hat import SenseHat

sense = SenseHat()
houses = ["Lovekyn", "Queens", "Stanley", "Taverner", "Walworth"]

print("What is your name?")
name = input()
houses = ["Lovekyn", "Queens", "Stanley", "Taverner", "Walworth"]
house = random.choice(houses)

if house == "Lovekyn":
    sense.show_message("Hello " + name + "! Welcome to " + house + " house! Fly like an eagle!")
elif house == "Queens":
    sense.show_message("Hello " + name + "! Welcome to " + house + " house! You are certainly royalty material!")
elif house == "Stanley":
    sense.show_message("Hello " + name + "! Welcome to " + house + " house!")
elif house == "Taverner":
    sense.show_message("Hello " + name + "! Welcome to " + house + " house!")
else:
    sense.show_message("Hello " + name + "! Welcome to " + house + " house! Eye of the tiger!")
    
