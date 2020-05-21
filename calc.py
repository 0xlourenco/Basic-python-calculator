print ''
x = raw_input('Select a number: ')
y = raw_input('Select another number: ')
print 'Numbers Selected: ' + x + ' and ' + y
num1 = float(x)
num2 = float(y)
print'''

		Select operation:
	1) +
	2) -
	3) *
	4) /

'''
w = input(':> ')
print w
if w==1:
	print num1 + num2
elif w==2:
	print num1 - num2
elif w==3:
	print num1 * num2
elif w==4:
	print num1 / num1
else:
	print 'Option not defined'
