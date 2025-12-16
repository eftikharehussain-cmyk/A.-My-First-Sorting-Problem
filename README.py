# A.-My-First-Sorting-Problem
t = int(input())
for _ in range(t):
	x, y = map(int, input().split())
	if x > y:
		x, y = y, x
	print(x, y)
