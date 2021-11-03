from collections import Counter
l = [int(input()) for _ in range(10)]
print(sum(l)//10, Counter(l).most_common()[0][0], sep='\n')