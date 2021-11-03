l7 = [0, 500] + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6 + [0]
l8 = [0, 512] + [256]*2 + [128]*4 + [64]*8 + [32]*16 + [0]
for _ in range(int(input())):
	a,b = map(int, input().split())
	print((l7[a if a<len(l7) else -1] + l8[b if b<len(l8) else -1])*10000)