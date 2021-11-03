l = list(filter(lambda e: e%2, [int(input()) for _ in range(7)]))
print(-1 if not(l) else '{}\n{}'.format(sum(l), min(l)))