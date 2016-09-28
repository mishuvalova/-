import os
import hashlib
import sys
import collections


def dup(top_dir):
  hashfile = collections.defaultdict(set)
  
  for dirp, _, files in os.walk(top_dir) :
    for filename in files :
      dpath = os.path.join(dirp, filename)
      if filename.startswith(('.','~')) or os.path.islink(dpath):
        continue
      hashd = hashlib.sha1()
      with open(dpath, mode = 'rb') as content:
        while True:
          data = content.read(1024)
          if not data:
            break
          hashd.update(data)
        hashfile[hashd.hexdigest()].add(os.path.relpath(dpath, top_dir))
        
  for files in hashfile.values():
    if len(files) != 1:
      print(':'.join(files))
      
def main():
  if len(sys.argv) != 2:
    sys.exit(1)
    
  top_dir = sys.argv[1]
  dup(top_dir)
  
if __name__== '__main__':
    main()import os
import hashlib
import sys
import collections


def dup(top_dir):
    hash_to_files = collections.defaultdict(set)
    for dirp, _, files in os.walk(top_dir):
        for filename in files:
            rel_path = os.path.join(dirp, filename)
            if filename.startswith(('.', '~')) or os.path.islink(rel_path):
                continue
            hashdoing = hashlib.sha1()
            with open(rel_path, mode='rb') as content:
                while True:
                    data = content.read(1024)
                    if not data:
                        break
                    hashdoing.update(data)
                hash_to_files[hashdoing.hexdigest()].
                add(os.path.relpath(rel_path, top_dir))
    for files in hash_to_files.values():
        if len(files) != 1:
            print(':'.join(files))


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    top_dir = sys.argv[1]
    dup(top_dir)
if __name__ == '__main__':
    main()
