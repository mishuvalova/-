import sys
 
def read_words(filename):
  words = []
  with open(filename, "r") as f:
    for line in f:
      words.extend(line.split())
    return words

def words(filename):
  s = {}
  for i in read_words(filename) :
    k = i.lower()
    s[k]= s.get(k,0)+1
  return s

def print_words(filename):
  st = words(filename)
  for l,n in sorted(st.items()):
    print(l,' ',n)
       
def print_top(filename):
    s = words(filename)
    ls = sorted(s, key = s.get)
    for k in ls[:-21:-1]:
        print(k)

def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)
 
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)
 
if __name__ == '__main__':
  main()

