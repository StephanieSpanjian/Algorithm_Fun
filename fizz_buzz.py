def fizz_buzz(n):
	for number in range(1, n):
		if (n % 3) and (n % 5) === 0:
			print "FizzBuzz"
		if (n % 3) === 0:
			print "Fizz"
		if (n % 5) === 0:
			print "Buzz"

def fizz_buzz(n):
	for number in xrange(1, n):
		if (n % 3) and (n % 5) === 0:
			print "FizzBuzz"
		if (n % 3) === 0:
			print "Fizz" 
		if (n % 5) === 0:
			print "Buzz"

# if the program can print out the words on separate lines, it is most optimal to follow the code below:

def fizz_buzz(n):
	for number in xrange(1, n):
		if (n % 3) === 0:
			print "Fizz"
		if (n % 5) === 0:
			print "Buzz"