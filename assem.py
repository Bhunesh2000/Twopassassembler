def pass1(line,optable,symtable,LC):
    words = line.split(" ")
    print("words=  " + str(words))
    if (words[0][0] != "/"):
        LC += 1
        for i in range(len(words)):
            if (len(words[i])!= 0):
                if (words[i][0] != "/"):
                    if (words[i][-1]!= ":"):
                        if words[i] in optable:
                            print(words[i] + " = " + optable[words[i]])
                        elif words[i] == "START":
                            print("START found")
                            LC = words[i + 1]
                        elif words[i] == "END":
                            print("End found")
                            break
                        elif not words[i].isdigit():
                            if (words[i] not in symtable):
                                symtable[words[i]] = ""
                    else:
                        if (words[i] not in symtable):
                            symtable[words[i][:-1]] = LC
                else:
                    break

    print("LC=" + str(LC))
    print("symbol table --> ", symtable)
    return symtable,LC

def pass2(line,optable,symtable,LC,filew):
    words=line.split(" ")
    print("words=  "+ str(words))
    strout=""
    if (words[0][0]!="/"):
        for i in range(len(words)):
            if (len(words[i]) != 0):
                if (words[i][0] != "/"):
                    if (words[i][-1] != ":"):
                        if words[i] in optable:
                            strout+=" "  + str(optable[words[i]])
                            print("opcode -- ",str(optable[words[i]]))
                        elif words[i] == "START":
                            print("START found")
                            LC = words[i + 1]
                        elif words[i] == "END":
                            print("End found")
                            break
                        elif words[i].isdigit():
                            strout+=" "+ str(bin(int(words[i]))[2:]).zfill(8)
                            print(" address -- ", str(bin(int(words[i]))[2:]))
                        else:
                            strout+=" " +str(bin(symtable[words[i]])[2:]).zfill(8)
                            print(" symbol -- ", str(bin(symtable[words[i]])[2:]))
                else:
                    break
        LC=LC+1
        strout=str(bin(LC)[2:]).zfill(4)+strout
        print(" LC-- ", str(bin(LC)[2:]))
        filew.writelines(strout)
        filew.writelines("\n")
        print(" written this -- ",strout," -- in the ouput file" )
    print("LC=" + str(LC))
    # print("symbol table --> ",symtable)
    return LC

def assembler():
    # filein=input("Enter the name of the input assembler language file")
    # fileout=input("Enter the name of the output machine language file")
    # fileop=input("Enter the name of the file containing opcodes")
    filein="inp3.txt"
    fileout="output.txt"
    fileop="opcodes.txt"
    filer=open(filein,"r")
    filew=open(fileout,"w")
    fileo=open(fileop,"r")
    optable={}
    symtable={}
    LC=0
    opcodelines=fileo.readlines()
    for opline in opcodelines:
        opline=opline.rstrip("\n")
        pairs=opline.split(" ")
        optable[pairs[1]]=pairs[0]
    print("optable=  "+str(optable))
    file=filer.readlines()
    print( "input ",file)
    for lines in file:
        symtable,LC=pass1(lines.rstrip("\n"),optable,symtable,LC)
    print("first pass finished")
    print("symbol table --> ",symtable)
    for i in symtable:
        if symtable[i]=="":
            LC += 1
            symtable[i]=LC
    print("symbol table --> ",symtable)
    print("pass 2 started")
    LC=0
    for lines in file:
        LC=pass2(lines.rstrip("\n"),optable,symtable,LC,filew)

assembler()
