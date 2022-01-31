n = int(input("Enter the year: " ))
if n % 4  == 0 and n % 400 == 0:
	print("TRUE")
elif n % 4 == 0 and n % 400 != 0:
	print("TRUE")
else:
	print("FALSE")