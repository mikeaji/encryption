
#empty list
array = []


#open file
files = open("sys.py","w")

#read into list
with open("sfs.py", "r+") as readsfile:
    for line in readsfile:
        array.append(line)


#modify line 52 - remove new line + add vrus
array[51] = array[51].rstrip() + "; print('virus')\n"


#add list to file
sfs = open("sfs.py", "w")

for line in array:
    sfs.write(line)

sfs.close()
