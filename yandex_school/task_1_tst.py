def sumOfTwo() -> int:
	return sum(int(num) for num in input().split(' '))

print(sumOfTwo())