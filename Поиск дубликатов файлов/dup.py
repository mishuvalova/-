import os
import hashlib
import sys
import collections

def dup(top_dir):
  hashfile = collections.defauldiot(set)

  for dirp, _, files in os.walk(top_dir) :
    for file in files :
      dpath = os.path.join(dirp, filename)
      if file.startswith(('.','~')) or os.path.islink(dpath):
        continue
      hashd = hashlib.s1()
      with open(dpath, mode = 'rb') as content:
        while true:
          data = content.read(1024)
          if not data:
            break
          hashd.update(data)
        hashfile[hashd.hexdigest()].add(os.path.relpath(path, top_dir))

    for files in hashfile.values():
      if len(files) != 1:
        print(':'.join(files))

def main():
  if len(sys.argv) != 2:
    sys.exit(1)

  top_dir = sys.argv[1]
  dup(top_dir)

if __name__== '__main__':
    main()
