
files = open("C:\\Users\\acer\\Documents\\GitHub\\Code\\Compiler Design Assignments\\LL(1) Grammar\\rules.txt", 'r')

non_terminals = []
right = []
for line in files:
    non_terminals.append(line.split()[0])
    right .append(line.split()[2])

corr_dict = {}
for i in range(len(non_terminals)):
    for j in range(len(right)):
        if i==j:
            corr_dict[non_terminals[i]] = right[j]

#print corr_dict
#print non_terminals

firsts_dict = {}

#for value in corr_dict.keys()

for key in corr_dict.keys():
    if corr_dict[key][0] not in non_terminals:
        firsts_dict[key] = corr_dict[key][0]
    for search in range(len(corr_dict[key])):
        if corr_dict[key][search]=="|" and (corr_dict[key][search+1] not in non_terminals):
            firsts_dict[key]+ corr_dict[key][search+1]

print firsts_dict




