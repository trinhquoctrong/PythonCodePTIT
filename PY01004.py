# nguyên tố
import math

def ngto(n):
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if(n % i == 0):
			return False
	return True

def gcd(a, b):
	while b > 0:
		c = b
		b = a % b
		a = c
	return a

t = int(input())
for x in range(t):
	n = int(input())
	k = 0
	for i in range(1, n):
		if gcd(n, i) == 1:
			k += 1
	if ngto(k) == True:
		print("YES")
	else:
		print("NO")
