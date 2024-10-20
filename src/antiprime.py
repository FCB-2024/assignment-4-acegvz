import sys 

def c(n):
	count = 0
	i = 1
	while i * i <= n:
		if n % i == 0:
			count = count + 1
			if i != n:
				count = count + 1
		i = i + 1
	return count

def a(n):
	max_div = 0
	for s in range (1, n):
		div_count = c(s)
		if div_count > max_div:
			max_div = div_count
	return c(n) >= max_div


def main():
	if len(sys.argv) != 2:
		print("error: antiprime.py <positive_integer>")
		return
	
	n = int(sys.argv[1])
		
	if n <= 0:
		print("error: antiprime.py <positive_integer>")
		return
	
	if a(n):
		print("anti-prime")
	else:
		print("not anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	main()

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
