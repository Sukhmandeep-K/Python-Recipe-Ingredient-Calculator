"""
This program gives the user the desired amount of ounces needed in order to make their recipe per serving.
"""
#This asks user for ingrdient no.1 name and ounces
first_ingredient = input("Enter ingredient 1:")
first_ounces = float(input("Ounces of " + first_ingredient + ":" ))

#This asks user for ingredient no.2 name and ounces
second_ingredient = input("Enter ingredient 2:")
second_ounces = float(input("Ounces of " + second_ingredient + ":"))

#This asks user for ingredient no.3 name and ounces
third_ingredient = input("Enter ingredient 3:")
third_ounces = float(input("Ounces of " + third_ingredient + ":"))

#This asks user for no. of servings
servings = int(input("Numbers of servings: "))

#This prints out input the user provided
print("Total ounces of " + first_ingredient + ": " + str(first_ounces * servings))
print("Total ounces of " + second_ingredient + ": " + str(second_ounces * servings))
print("Total ounces of " + third_ingredient + ": " + str(third_ounces * servings))