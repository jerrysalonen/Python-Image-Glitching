import random
import os

filepath = ""
fileSize = int(os.path.getsize(filepath))

# Injects random amount of bytes (between b1 and b2) to a random location.
def injectBytes(b1, b2):
    offset = random.randint(int((fileSize/8)), fileSize)
    b = fh.read(random.randint(b1, b2))

    fh.seek(offset)
    fh.write(b)

# Takes a random chunk of bytes (between b1 and b2) and injects them in reverse
def reverseBytes(b1, b2):
    offset = random.randint(int((fileSize/8)), fileSize)
    fh.seek(offset)

    b = fh.read(random.randint(b1, b2))
    b = str(b)[::-1]
    b = b.encode("utf-8")

    fh.write(b)

# Injects random bytes (between b1 and b2) to a random location. Includes an optional seed
def injectGrabage(b1, b2, seed = 500):
    random.seed(seed)
    offset = random.randint(int((fileSize/8)), fileSize)
    fh.seek(offset)

    fh.write(bytes(random.randint(b1, b2)))

# Fills a random spot in file with zero-bytes based on given parameter.
def fillWithZero(size):
    offset = random.randint(int((fileSize/8)), fileSize)
    fh.seek(offset)
    b = ""

    for x in range(size):
        b += str(0)
    
    b = b.encode("utf-8")
    fh.write(b)

fh = open(filepath, "r+b")

# Below is an example of how you could use this script.
repeat = 10
for x in range(repeat):
    reverseBytes(10, 20)
    injectGrabage(10, 43, 9492)
    injectBytes(10, 35)
    injectBytes(23, 55)
    injectBytes(8, 15)
    fillWithZero(1)

fh.close()