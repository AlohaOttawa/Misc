# x = [1,2,3]
x = 'test'
def func(x):
	# x[1] = 42
	x = 'something else'
	print(x)
func(x)
print(x)