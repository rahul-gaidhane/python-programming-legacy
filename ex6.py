#first the string is evaluated then is assinged to variable x
x = 'There are %d types of people.' % 10
#string is assinged to both the variables
binary = "binary"
do_not = "don't"
#again the string is evaluated and then is assinged to y
y = "Those who know %s and those who %s." % (binary, do_not)
#variable x and y is printed
print x
print y
#string is printed
print "I said: %r." % x
print "I also said: '%s'." % y
#varaible is assinged the boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#how is this performed
print joke_evaluation % hilarious
#string are assinged to the variables
w = "this is the left side of..."
e = "a string with a right side."
#string are added and printed , they get concatenated
print w + e
