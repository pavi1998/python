a = input()
m = [ ch  for i, ch in enumerate(a) if ch not in a[:i]]
print(''.join(m))
