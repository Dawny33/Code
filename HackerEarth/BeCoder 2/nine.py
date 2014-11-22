
from itertools import combinations
 
def is_good(n):

    return 1 + ((int(n) - 1) % 9) == 9
 
 
def generate_subsequences(n):
    subsequences = []
    combinations_list = []
    index = 4
#Generate all combinations
    while index > 0:
        combinations_list.append(list(combinations(str(n), index)))
        index -= 1
#Formatting combinations
    for index in combinations_list:
        for combination in index:
            subsequences.append(''.join(combination))
    return subsequences
 
 
if __name__ == '__main__':
#The modulo
    modulo = ((10 ** 9) + 7)
#Get number of cases
    cases = int(raw_input())
    while cases > 0:
        value = raw_input()
        good_subsequences = 0
        for sub in generate_subsequences(value):
            if is_good(sub):
                good_subsequences += 1
        print (good_subsequences % modulo)-1
        cases -= 1 
