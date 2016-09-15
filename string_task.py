# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Example input: 'read'
# Example output: 'reading'
def verbing(s):
  length = len(s)
  if length >= 3:
    if s[-3:] == 'ing':
      return s +'ly'
    else:
      return s + 'ing'
    
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
#
# Example input: 'This dinner is not that bad!'
# Example output: 'This dinner is good!'
def not_bad(s):
  nn = s.find('not')
  nb = s.find('bad')
  if nn != -1 and nb != -1 and nb > nn:
    s = s[:nn] + 'good' + s[nb +3:]   
  return s
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
#
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Example input: 'abcd', 'xy'
# Example output: 'abxcdy'

def front_back(a, b):
  l1 = len(a)
  l2 = len(b)
  i1 = l1//2 - l1%2
  i2 = l2//2 - l2%2
  a1 = a[0:i1]
  a2 = a[i1:]
  b1 = b[0:i2]
  b2 = b[i2:]
  return a1 + b1 + a2 + b2

