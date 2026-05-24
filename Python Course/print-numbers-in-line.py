#print numbers next to each other (same line):

for i in range (1,6):
    line=" "
    for j in range(1,i+1):
        line=line + str(j)
    print(line)
