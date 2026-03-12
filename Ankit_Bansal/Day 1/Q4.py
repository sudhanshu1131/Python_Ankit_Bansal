# write a program which takes city name from user input. irrespective of in which case user enters the city name, print the city name in camel case meaning first letter should be capital and rest in small.
city = input("Enter your city name: ")
print(city.capitalize())

#solution 1:
city_name = input("Enter the city name: ")

# Convert the city name to lowercase
city_name = city_name.lower()

# Capitalize the first letter
city_name = city_name[0].upper() + city_name[1:]

print("City name in camel case:", city_name)




#solution 2:
city_name = input("Enter the city name: ")

# Convert the city name to lowercase
city_name = city_name.lower()

# Capitalize the first letter
city_name = city_name.capitalize()

print("City name in camel case:", city_name)