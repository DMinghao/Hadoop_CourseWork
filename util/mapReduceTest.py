import os
import sys

target = ""
dataFile = ""

if len(sys.argv) >= 3:
    target = f"../{sys.argv[1]}"
    dataFile = f"{target}/{sys.argv[2]}" 

if target == "": 
    while True: 
        target = input("Enter your target folder: ") 
        if os.path.isdir(f"../{target}"): 
            target = f"../{target}"
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