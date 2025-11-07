# Lists - have  brackets [] - everything inside is called an item

mr_robot_character = ["Elliot", "Mr Robot", "Tyrell wellick", "Darlene"]

print (mr_robot_character[0]) # returns only ther first item
print (mr_robot_character[0:3]) # returns the first number given until right before the last number
print (mr_robot_character[0:]) # returns everything from the 0
print (mr_robot_character[:1]) # everything before 1
print (mr_robot_character[-1]) # grabs the last item

print(len(mr_robot_character)) # counts the item in the list
mr_robot_character.append("whiterose") # add an item to the end of our list
print(mr_robot_character)
mr_robot_character.insert(3, "Gideon")
print(mr_robot_character)
mr_robot_character.pop() # to remove an item in the list; default is the last item
print(mr_robot_character)
mr_robot_character.pop(3) # to remove a specific itme in the list
print(mr_robot_character)

dark_army = ['whiterose', 'F_agents']

the_revolution = mr_robot_character + dark_army # combined list

print(the_revolution)

iq_check = ["Elliot", 119], ["Mr Robot", 119], ["Tyrell wellick", 110]
iq_deduction = iq_check[2][1] 

print(iq_deduction)

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[2][2])