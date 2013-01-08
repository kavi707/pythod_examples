def add(a, b):
	return a+b

def substract(a, b):
	return b-a

def multiply(a, b):
	return a*b

def divide(a, b):
	if b == 0:
		return "Syntax Error"
	else:
		return a/b

def getInputs():
	print " "
	print " "
	print "Welcome to calculator from python"
	print "your options are:"
    	print " "
    	print "1) Addition"
    	print "2) Subtraction"
    	print "3) Multiplication"
    	print "4) Division"
    	print "5) Quit calculator.py"
    	print " "
	return input ("Choose your option: ")


loop = 1
choice = 0
r = 0
while loop == 1:
	choice = getInputs()
	if choice == 1:
		r = add(input("Add this: "), input("to this: "))
		print "Added Result:", r
	elif choice == 2: 
		r = substract(input("Substract this: "), input("from this: "))
		print "Substract Result:",r
	elif choice == 3:
		r = multiply(input("Multiply this: "), input("from this: "))
		print "Multiplied Result:",r
	elif choice == 4:
		r = divide(input("Divide this: "), input("from this: "))
		print "Divided Result:",r
	elif choice == 5:
		loop = 0
	else:
		print "Error input"


