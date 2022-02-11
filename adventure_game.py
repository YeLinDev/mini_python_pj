print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
print("Your Choice: ")
first = input("")
if first.upper()=="MATCH":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
    print("Your Choice: ")
    second = input("")
    if second.upper()=="RUN":
        print("You run into the forest")
    elif second.upper()=="HIDE":
        print("You hide under the tree's branch")
    else:
        print("Wrong Input")
elif first.upper()=="FLASHLIGHT":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    print("Your Choice: ")
    third = input("")
    if third.upper()=="FOLLOW":
        print("You follow the path and sees the lion")
    elif third.upper()=="LOOK":
        print("You looks at the tree")
    else:
        print("Wrong Input")
else:
    print("Wrong Input")

#print("Your Choice: ")
#second = input("")
#if second.upper()==""