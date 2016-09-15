def remove_adjacent(lst):
  l = []
  for num in lst:
    if len(l) == 0 or num != l[-1]:
      l.append(num)
      
  return l

def linear_merge(lst1, lst2):
  l = []
  while len(lst1) and len(lst2):
    if lst1[0] < lst2[0]:
      l.append(lst1.pop(0))
      
    else:
      l.append(lst2.pop(0))
