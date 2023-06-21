import re
default = re.compile(r'&?(\w+)(=)?(\w+)?')
parameter = re.compile(r'\(P,(\d+)\)')

class macroPass2:
    def __init__(self):
        self.macroNameTable = {} #hash map. value is an array containing pp,kp,mdtp,kpdtp
        self.macroDefTable = [] #simple array
        self.keywordParamDefTable = {} #Key-Name of macro. Value- an array containing tuples(name,value) -- KPDTAB
        self.paramNameTable = {} # key-name of function,value-an array containing name of params
        self.ICFile = open('intermediateCode.txt',mode='r')
        self.macroDefTableFile = open('macroDefTable.txt',mode='r')
        self.macroNameTableFile = open('macroNameTable.txt',mode='r')
        self.keywordParamDefTableFile = open('keywordParamDefTable.txt',mode='r')
        self.paramNameTableFile = open('paramNameTable.txt',mode='r')
        self.output = []
        self.outputFile = open('output.txt',mode='w')
    
    def readMacroDefTable(self):
        self.macroDefTable.append([])
        for line in self.macroDefTableFile.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            self.macroDefTable.append(line[:-1])
    
    def readMacroNameTable(self):
        skipFirstLine = False
        for line in self.macroNameTableFile.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            if skipFirstLine == False:
                skipFirstLine = True
                continue
            else:
                self.macroNameTable[line[0]] = line[1:]
    
    def readKeywordParamDefTable(self):
        lines = self.keywordParamDefTableFile.readlines()
        for macroName,value in self.macroNameTable.items():
            numOfKeywordParam = int(value[1])
            kpdtp = int(value[3])
            self.keywordParamDefTable[macroName] = {}
            for i in range(kpdtp,kpdtp + numOfKeywordParam):
                line = lines[i-1].strip('\n').split('\t')
                self.keywordParamDefTable[macroName][line[0]] = line[1]
    
    def readParamNameTable(self):
        for line in self.paramNameTableFile.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            self.paramNameTable[line[0]] = line[1:]
    
    
    def createAPTAB(self,macroName):
        APTAB = []
        APTAB.append(self.paramNameTable[macroName])
        APTAB.append([])
        APTAB.append([])
        keywordParamDict = self.keywordParamDefTable[macroName]
        for param in APTAB[0]:
            if param in keywordParamDict:
                APTAB[1].append(keywordParamDict[param])
                if keywordParamDict[param] == "----":
                    APTAB[2].append(None)
                else:
                    APTAB[2].append(keywordParamDict[param])
            else:
                APTAB[1].append(None)
                APTAB[2].append(None)
        return APTAB

    def printAPTAB(self,APTAB):
        print("APTAB:")
        for i in range(len(APTAB[2])):
            print(i+1,APTAB[2][i],sep="\t")
        print()
    
    def tupleToParam(self,line:list,APTAB:list) -> list:
        result = []
        for part in line:
            find = parameter.search(part)
            if find == None:
                result.append(part)
            else:
                idx = int(find.group(1)) - 1
                result.append(APTAB[2][idx])
        return result
        

    def parseFile(self):
        for line in self.ICFile.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            part_1 = line[0]

            if part_1 not in self.macroNameTable:
                self.output.append(line)
            else:
                #Pass actual parameters
                part_2 = line[1].split(', ')
                APTAB = self.createAPTAB(part_1)
                for param in range(len(part_2)):
                    find = default.search(part_2[param])
                    
                    if find.group(2) == None:
                        APTAB[2][param] = find.group(1)
                    else:
                        idx = APTAB[0].index(find.group(1))
                        APTAB[2][idx] = find.group(3)
                #write macro definition with actual parameters
                mdtp = int(self.macroNameTable[part_1][2])
                print(*line,sep="\t")
                self.printAPTAB(APTAB)
                for macroDefLine in self.macroDefTable[mdtp:]:
                    if macroDefLine[0] == "MEND":
                        break
                    else:
                        self.output.append(self.tupleToParam(macroDefLine,APTAB))
                        print(*self.tupleToParam(macroDefLine,APTAB),sep="\t")
                print('\n')
        self.writeOutputFile()
        self.keywordParamDefTableFile.close()
        self.macroDefTableFile.close()
        self.macroNameTableFile.close()
        self.paramNameTableFile.close()
    
    def writeOutputFile(self):
        for value in self.output:
            line = "\t".join(value)
            line += "\n"
            self.outputFile.write(line)
        self.outputFile.close
