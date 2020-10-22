filename = "sfs.py"
file = open(filename, "r")
line_list = file.readlines()     
file.close()

file = open(filename, "w")
count = 0; 
for line_num in line_list:
        count = count + 1
        if (count== 52):
                line_num = line_num.replace('\n','; print( "Virus" )\n')
                
        file.write(line_num)

                 
file.close()


