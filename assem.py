filein="input.txt"
fileout="output.txt"
filer=open(filein,"r")
filew=open(fileout,"a")
lineno=0
file=filer.readlines()
print(file)
for lines in file:
    # print(lines)
    r=lines.split(" ")
    # print(r)
    for i in range(len(r)):
        print(str(i) + " " + r[i])
        filew.write(r[i]+"\n")
