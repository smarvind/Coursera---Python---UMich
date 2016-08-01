l = 0
s = 10000
while True:
		
	y = raw_input("enter your number")
	if y == 'done':
		break
	x = int(y)
	
	if x < s:
		s = x
		print s

	if x > l and x >= s:
		l = x
		print l

print l, s
