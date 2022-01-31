def factorialize():
	x = 1
	n = int(input("please enter a number:" ))
	if n == 1:
	    print (n)
	elif n <= 0:
	    print("it cannot be factorized")
	else:
	    for y in range(1,n+1):
	        x = x * y
	    print(f"the factorial of {n} is {x} " )


factorialize()
