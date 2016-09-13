def remove_adjacent(lst):
  k = 1
  while k < len(lst):    
    if lst[k] == lst[k-1]:
      lst.pop(k)
      k = k - 1  
    k = k + 1
  return lst
def linear_merge(lst1, lst2):
  lst3=sorted(lst1+lst2)
  return lst3
