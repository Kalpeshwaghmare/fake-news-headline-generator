# 1- import the random module
import random

# 2- create subjects
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Elon Musk",
    "Greta Thunberg",           
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Taylor Swift",
    "Bill Gates",
]

actions = [ 
    "is launching a new product",
    "is starting a new charity",
    "is moving to Mars",
    "is retiring from their career",
    "is getting married",
    "is running for president",
    "is opening a new restaurant",
    "is writing a new book",
]

places_or_things = [
    "in Antarctica",
    "in a secret underground bunker",
    "on a private island",
    "in a haunted mansion",
    "in the metaverse",
    "on a spaceship",
    "in a virtual reality game",
    "in a parallel universe",
]

# 3 start the headline generation loop
while True:

 # 4- generate a random headline
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}!"
    
 # 5- print the generated headline
    print("\n" + headline)
    
# 6- ask if the user wants to generate another headline
    another = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# 7- end the program
print("Thank you for using the Fake News Generator!")