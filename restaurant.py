#Baylor Wroblewski
#CS 175L
#Restaurant

vegetarian = False
vegan = False
glutenfree = False

#receives input from user
ask_vegetarian = input("Is anyone in your party a vegetarian? ")
if ask_vegetarian == "yes":
    vegetarian = True
    
ask_vegan = input("Is anyone in your party a vegan? ")
if ask_vegan == "yes":
    vegan = True
    
ask_glutenfree = input("Is anyone in your party gluten free? ")
if ask_glutenfree == "yes":
    glutenfree = True

#prints out available restaurants
print("\nHere are your restaurant choices: ")

if vegetarian == False and vegan == False and glutenfree == False:
    print("Joe's Gourmet Burgers")

if vegan == False and glutenfree == False:
    print("Mama's Fine Italian")

if vegan == False:
    print("Main Street Pizza Company")

print("Corner Cafe")
print("The Chef's Kicthen")

print("\nEnjoy your meal!")
