def pass1(line,optable,symtable,littable,pooltable,LC):
    words=line.split(" ")
    print("words=  "+ str(words))
    for i in range(len(words)-1):
        if words[i] in optable :
            print( words[i] +" "+ optable[words[i]])
            # symtable[]
        elif words[i]=="START":
            print("START found")
            LC   = words[i + 1]
        else :
            symtable[words[i]]=""
        print("LC=" + str(LC))
    print(symtable)
    return optable,symtable,littable,pooltable,LC


def assembler():
    # filein=input("Enter the name of the input assembler language file")
    # fileout=input("Enter the name of the output machine language file")
    # fileop=input("Enter the name of the file containing opcodes")
    filein="input2.txt"
    fileout="output.txt"
    fileop="opcodes.txt"
    filer=open(filein,"r")
    filew=open(fileout,"a")
    fileo=open(fileop,"r")
    optable={}
    symtable={}
    littable={}
    pooltable={}
    LC=0
    opcodelines=fileo.readlines()
    for opline in opcodelines:
        opline=opline.rstrip("\n")
        pairs=opline.split(" ")
        optable[pairs[1]]=pairs[0]
    print("optable=  "+str(optable))
    file=filer.readlines()
    print(file)
    for lines in file:
        optable,symtable,littable,pooltable,LC=pass1(lines.rstrip("\n"),optable,symtable,littable,pooltable,LC)


assembler()
