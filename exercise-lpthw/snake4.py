#we gave the number value to the variable name "car"
cars = 100
#we gave variable name a number value too
space_in_a_car = 4.0
#same here with "drivers"
drivers = 30.0
#and also with "passengers"
passengers = 90
#we created the variable "cars_not_driven" and assigns two variables defined previously to it
#the result is the value which has been assigned to them previously then all assigned to the
#new variable created. Thus the new variable "cars_not_driven" holds the value of "cars" and "drivers"
#which are apparently being divided
cars_not_driven = cars - drivers
#created a new variable "cars_driven" and assign to it a previously defined variable name
#meaning were are assigning whatever value "drivers" hold or has been assigned
cars_driven = drivers
#the same concept as in the 5th comment but different variable names and assignments
#the variable "carpool_capacity" equals the value of the variable "cars_driven" and "space_in_a_car"
#which are obviously being multiplied
carpool_capacity = cars_driven * space_in_a_car
#same idia with the abbove comment but in this case the values are being divided
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, " in each car."



#the code wont run. in line 8 the "car_pool_capacity" was not assigned any value 
#and "passenger" too was not assigned any value but "passengers"

i = 534.0
x = 443
j = 30.0
z = j + x * i


print i * j * x
print j / x
print z - x


