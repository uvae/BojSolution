def totalTime(graph, dis, src, des):
	s = [0] 

for t in range(int(input())):
	n, k = map(int, input().split())
	dis = [0] + list(map(int, input().split()))

	graph = {}

	for i in range(1, n+1):
		graph[str(i)] = set()

	for i in range(k):
		s, d = input().split()
		graph[s] = set(d)
	
	print(totalTime(graph, dis, '1', input()))