from decimal import *

def increase(x = input('What salary?: ')):	
	y = 2010
	q = x
	for i in range(21):
		print y, "\t", "%.2f" % x, "\t",
		print "%.2f" % q
		x = x * 1.02
		q = q + x
		y = y + 1

increase()
	
