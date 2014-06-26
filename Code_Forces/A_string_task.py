T = raw_input().lower()

vowels = "aeiouy"
output = ""

for i in range(0,len(T)):
    if T[i] not in vowels:
        output += "." + T[i]

print output
