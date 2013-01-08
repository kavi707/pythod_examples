a = 10
while a > 0:
	print a
	if a > 5:
		print "Big number"
	elif a % 2 != 0:
		print "This is an odd number"
		print "It isn't greater than 5, either"
	else:
		print "This isn't a number greater than 5"
		print "nor is it odd"
		print "feeling special?"
	a = a - 1
	print "We just made 'a' one less than what it was!"
	print "and unless a is not greater than 0, we'll do the loop again."
print "Well, it seems as if 'a' is now no bigger than 0!"
print "the loop is now over, and without further adue, so is this program!"
