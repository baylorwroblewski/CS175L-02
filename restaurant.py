#Baylor Wroblewski
#CS 175L
#Restaurant Version 2

again = True

#receives input from user
while again == True:
    vegetarian = False
    vegan = False
    glutenfree = False
    ask_vegetarian = input("Is anyone in your party a vegetarian? ")
    if ask_vegetarian == "yes" or ask_vegetarian == "Yes":
        vegetarian = True
    ask_vegan = input("Is anyone in your party a vegan? ")
    if ask_vegan == "yes" or ask_vegan == "Yes":
        vegan = True
    ask_glutenfree = input("Is anyone in your party gluten free? ")
    if ask_glutenfree == "yes" or ask_glutenfree == "Yes":
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

    again = input("\nEnter 'yes' to begin another search, enter 'no' if you are finished! ")
    if again == "yes" or again == "Yes":
        again = True
    else:
        again = False
        print("Enjoy your meal!")
