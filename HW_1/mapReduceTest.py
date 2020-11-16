import os
import sys

dataFile = sys.argv[1]

os.system(f"python writer.py {dataFile} | python mapper.py | python reducer.py")