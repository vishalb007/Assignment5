def fact(no):
	if(no == 0):
		return 1
	return no * fact(no-1)

def main():
	num=int(input("Enter the number : "))
	ret = fact(num)
	print ("Factorial is : ",ret)

if (__name__=="__main__"):
	main()