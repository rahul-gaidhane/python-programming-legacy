my_name = 'Zed A.Shaw'
my_age = 35
my_height = 74
height_in_cm = my_height * 2.54
my_weight = 180
weight_in_kg = my_weight * 0.4532
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s" %  my_name
print "He's %d inches tall." % my_height
print "He's %r centimeters." % height_in_cm
print "He's %d pounds heavy." % my_weight
print "He's %r kilograms heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
