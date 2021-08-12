#number of cars is 100
cars = 100
#number of passengers accomodated by each car
space_in_a_car = 4
#drivers available
drivers = 30
#number of passengers available
passengers = 90
#cars not being driven
cars_not_driven = cars - drivers
#cars can be driven due to avialability of drivers
cars_driven = drivers
#how much passengers can be driven
carpool_capacity = cars_driven * space_in_a_car
# number of passengers can be driven per car
average_passengers_per_car = passengers / cars_driven
#car_pool_capacity is a variable but not defined

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there."%"kk"
