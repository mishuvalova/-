def remove_adjacent(lst):
  if lst:
    l = [lst[0]]
    for k in range(1,len(lst)):
      if lst[k-1] != lst[k]:
        l.append(lst[k])
    return l  
  return []

def linear_merge(lst1, lst2):
  l = []
  i1 = 0
  i2 = 0
  while i1 < len(lst1) and i2 < len(lst2):
    if lst1[i1] < lst2[i2]:
      l.append(lst1[i1])
      i1 = i1 + 1
    else:
      l.append(lst2[i2])
      i2 = i2 + 1
  l.extend(lst1[i1:])
  l.extend(lst2[i2:])
  return l
