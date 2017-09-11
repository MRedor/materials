# dir(<module_name>) -- list content "names" defined by module

import math  # import entire module
from os import walk  # import single "name" (function/submodule)
from os import path
from math import pi as PI
from hashlib import sha1 as hasher  # import name with synonym

print("Sqrt: ", math.sqrt(9))
print("Traversal:")
for _, _, files in walk(".."):
    print("\t", files)

hasher = hasher()
hasher.update(b"chunk1")
hasher.update(b"chunk2")
hasher.update("chunk3".encode('utf-8'))
print(hasher.hexdigest())

# to get encoding of file, use encoding method
# with open(filename) as f:
#     print(f.encoding)
# to open file with binary mode, use mode = 'rb'
# with open(filename, mode='rb') as f:
#     hasher = hasher()
#     hasher.update(f.read(1024))
#     return hasher.digest() # digest of first min(1024, filesize) bytes of
# file
