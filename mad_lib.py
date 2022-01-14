#this is first question appear before entering the data
print("Please enter the following: ")

#these are user's data inputs
first_name= input("first name: ")
last_name= input("last name: ")
female_name= input("female name: ")
noun= input("noun: ")
noun_1= input("noun: ")
adjective= input("adjective: ")
verb= input("verb: ")
animals= input("animals: ")
animals_2= input("animals: ")
place= input("place: ") 
place_2 = input("place: ")
fruit= input("fruit: ")

print()
#this is the your intro
print("Your story is: ")
print()

#this is the story
output = "Once upon a time in {9}, There is a person named {0} {1}. He has a friend called {2}. One day they were {6} in the {10}, they {6} {7} and {8} running to the jungle. Then they {6} after them and saw a {11} tree. They {6} the fruits from that tree".format(first_name.capitalize(), last_name.capitalize(), female_name.capitalize(), noun, noun_1, adjective, verb, animals, animals_2, place, place_2, fruit)
print(output)
