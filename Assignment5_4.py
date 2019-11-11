def sum(num):
	if(num==0):
		return 0
	else:	
		return (num%10) + sum(num//10)

def main():
	num=int(input("Enter the number : "))
	ret=sum(num)
	print("Sum is : ",ret)

if (__name__=="__main__"):
	main()