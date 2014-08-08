f = open("C:\\Users\\acer\\Desktop\\Compiler Design\\simple_c_program.c", 'r')

arr = []
for line in f:
    for i in line.split():
        arr.append(i)

#print type(arr[8])        

char_arr = []
for token in arr:
    for ch in token:
        char_arr.append(ch)

#print char_arr

#For identifying integer literals.
num = "023456789"
symbols = "+-/%*"
det_lits = []
#print type(det_lits)
for fin in range(len(char_arr)):
    if (char_arr[fin] in num) and (char_arr[fin-1] not in symbols):
        det_lits.append(char_arr[fin])
print det_lits

#for multi-digit numbers.        
for fin3 in range(len(char_arr)):
    if (char_arr[fin3] in num):
        buff = [num]
        for p in range(len(char_arr[fin3:])):
            if (char_arr[p] in num):
                buff.append(char_arr[p])
print buff

#For identifying string literals.
str_lits = []
found = False
buff_str = ""
for ij in range(len(char_arr)):
    for fin2 in range(ij):
        if (char_arr[fin2] == '"'):
            flag = fin2+1
            while char_arr[flag] != '"' and not found:
                str_lits.append(char_arr[flag])
                str_lits.append(buff_str)
                flag += 1
                if char_arr[flag] == '"':
                    found = True
print str_lits



        

   

