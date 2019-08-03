v = input()
bb = [ ch  for i, ch in enumerate(v) if ch not in v[:i]]
print(''.join(bb))
