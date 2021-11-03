stack, res, before = [], 0, ''

for s in input():
	if(s == '('): stack.append(1)
	else:
		stack.pop()
		if(before == '('): res += stack.count(1)
		else: res += 1

	before = s

print(res)