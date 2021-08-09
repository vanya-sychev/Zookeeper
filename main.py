from animals import *


list_of_animals = [camel, lion, deer, goose, bat, rabbit]

number_of_habitats = 0

while number_of_habitats != "exit":
    number_of_habitats = input("Please enter the number of the habitat you"
                               " would like to view: ")

    if number_of_habitats != "exit":
        print(list_of_animals[int(number_of_habitats)])

print("See you later!")
