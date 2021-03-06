import os
import sys

target = ""
dataFile = ""
BASE_PATH ="../"

if len(sys.argv) >= 3:
    target = f"{BASE_PATH}{sys.argv[1]}"
    dataFile = f"{target}/{sys.argv[2]}" 
    if not os.path.isdir(target) and not os.path.isfile(dataFile): 
        print("Target Folder or Data File not found")
        sys.exit(-1)

if target == "": 
    while True: 
        target = input("Enter your target folder: ") 
        if os.path.isdir(f"{BASE_PATH}{target}"): 
            target = f"{BASE_PATH}{target}"
            break
        else:
            print("Target Folder Not Found") 

if dataFile == "": 
    while True: 
        dataFile = input("Enter your data file: ") 
        if os.path.isfile(f"{target}/{dataFile}"): 
            dataFile = f"{target}/{dataFile}" 
            break
        else:
            print("Data File Not Found") 

print(f"{target}")
print(f"{dataFile}") 

os.system(f"python writer.py {dataFile} | python {target}/mapper.py | python {target}/reducer.py") 