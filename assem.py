def OPCODE_ARG_CHK(WORDS):
    ZERO_ARG = ["CLA","STP" ]
    ONE_ARG = ["LAC","SAC","ADD","SUB","BRZ","BRN","BRP","INP","DSP","MUL","DIV"]
    if( WORDS[0] in ZERO_ARG ):
        if( len(WORDS) > 1 ):
            return 1
    elif( WORDS[0] in ONE_ARG ):
        if( len(WORDS) > 2 ):
            return 1
        elif( len(WORDS) < 2 ):
            return -1
    return 0

def pass1(line,optable,symtable,LC):
    ERROR_CODE = ""
    words=line.split(" ")
    while " " in words :
        del words[ words.index( " " ) ]
    while "" in words :
        del words[ words.index( "" ) ]
    print("words=  "+ str(words))

    for i in range(len(words)):
        if (words[i][-1] != ":"):
            if words[i] in optable:
                print(words[i] + " = " + optable[words[i]])
                if( OPCODE_ARG_CHK( words[i:] ) == -1 ):
                    print( "ERROR[04] > line" , LC  )
                    return symtable,LC,"04"
                if( OPCODE_ARG_CHK( words[i:] ) == 1 ):
                    print( "ERROR[04] > line" , LC  )
                    return symtable,LC,"05"
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
    LC += 1
    print("LC=" + str(LC))
    print("symbol table --> ",symtable)
    return symtable,LC,ERROR_CODE


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
    filew=open(fileout,"a")
    fileo=open(fileop,"r")
    optable={}
    symtable={}
    LC=0
    opcodelines=fileo.readlines()
    for opline in opcodelines:
        opline=opline.rstrip("\n")
        pairs=opline.split(" ")
        optable[pairs[1]]=pairs[0]
    #print("optable=  "+str(optable))
    file=filer.readlines()
    #print( "input ",file)
    ERROR_FLAG=""
    for lines in file:
        #COMMENT REMOVER
        if( lines.find( " //" ) != -1 ):
            lines = lines.replace( lines[lines.find( " //" ):] , "" )
        if( lines.find( "//" ) != -1 ):
            lines = lines.replace( lines[lines.find( "//" ):] , "" )
        #EMPTY LINE CHECKER
        if( lines != "" ):
            #PASSING LINE TO PASS1
            symtable,LC,ERROR_CODE=pass1(lines.rstrip("\n"),optable,symtable,LC)
        #ERROR RETURNED CHECK
        if ERROR_CODE != "":
            return 0
    #print("first pass finished")
    #print("symbol table --> ",symtable)
    for i in symtable:
        if symtable[i]=="":
            symtable[i]=LC
            LC+=1
    print("symbol table --> ",symtable)
    print("pass 2 started")
    LC=0
    for lines in file:
        LC=pass2(lines.rstrip("\n"),optable,symtable,LC,filew)
assembler()
