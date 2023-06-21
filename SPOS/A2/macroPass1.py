import re
default = re.compile(r'&(\w+)(=)?(\w+)?')
endline = "\n"
tab = "\t"

class macroPass1:
    def __init__(self):
        self.macroNameTable = {} #hash map.key-name of macro, value is an array containing pp,kp,mdtp,kpdtp
        self.macroDefTable = [] #simple array
        self.macroDefTablePointer = 1
        self.keywordParamDefTable = [] #Tuples(name,value) -- KPDTAB
        self.keyParamDefTabPointer = 1 #kpdtp
        self.paramNameTable = {} # key-name of macro,value-an array containing name of params
        self.inputFile = open('input.txt',mode="r")
        self.ICpointer = 0
        self.ICFile = open('intermediateCode.txt',mode='w')
        self.macroDefTableFile = open('macroDefTable.txt',mode='w')
        self.macroNameTableFile = open('macroNameTable.txt',mode='w')
        self.keywordParamDefTableFile = open('keywordParamDefTable.txt',mode='w')
        self.paramNameTableFile = open('paramNameTable.txt',mode='w')
    
    #input:param_name,current_macro output:(P,index)
    def covertToTuple(self,param,current_macro):
        id = self.paramNameTable[current_macro].index(param) + 1
        return "(P," + str(id) + ")"

    def parseFile(self):
        lines = self.inputFile.readlines()
        inMacroDefinition = False
        currentMacroName = None
        for line in lines:
            line = line.strip('\n')
            line = line.split('\t')
            part_1 = line[0]
            if part_1 == "START":
                break
            self.ICpointer += 1 
            part_2 = []
            if len(line) > 1:
                part_2 = line[1].split(', ')
            
            if part_1 == "MACRO":
                inMacroDefinition = True
                continue
            elif inMacroDefinition == True:
                self.paramNameTable[part_1] = []
                currentMacroName = part_1
                positionalParamCount = 0
                keywordParamCount = 0
                for param in part_2:
                    find = default.search(param)
                    self.paramNameTable[part_1].append(find.groups()[0])
                    if find.group(2) == None:
                        positionalParamCount += 1
                    else:
                        keywordParamCount += 1
                        
                        if find.group(3) == None:
                            self.keywordParamDefTable.append((find.group(1),"----"))
                        else:
                            self.keywordParamDefTable.append((find.group(1),find.group(3)))
                inMacroDefinition = False
                if keywordParamCount == 0:
                    self.macroNameTable[part_1] = [positionalParamCount,keywordParamCount,self.macroDefTablePointer,0]
                else:
                    self.macroNameTable[part_1] = [positionalParamCount,keywordParamCount,self.macroDefTablePointer,self.keyParamDefTabPointer]
                self.keyParamDefTabPointer += keywordParamCount
            elif part_1 == "MEND":
                self.macroDefTable.append([])
                self.macroDefTable[-1].append("MEND")
                self.macroDefTablePointer += 1
                currentMacroName = None
            else:
                self.macroDefTable.append([])
                self.macroDefTable[-1].append(part_1)
                for param in part_2:
                    find = default.search(param)
                    if find != None:
                        self.macroDefTable[-1].append(self.covertToTuple(find.group(1),currentMacroName))
                    else:
                        self.macroDefTable[-1].append(param)

                self.macroDefTablePointer += 1
        #Write the Intermediate Code file
        while self.ICpointer < len(lines):
            line = lines[self.ICpointer]
            self.ICFile.write(line)
            self.ICpointer += 1
        self.ICFile.close()
        self.inputFile.close()
    
    def writeKeywordParamDefTable(self):
        print("\nKeyword Parameter Default Table:")
        counter = 1
        for value in self.keywordParamDefTable:
            line = value[0] + tab + value[1] + endline
            self.keywordParamDefTableFile.write(line)
            print(counter,line,end="",sep="\t")
            counter += 1
        self.keywordParamDefTableFile.close()

    def writeMacroNameTable(self):
        line = "Name" + tab + "PP" + tab + "KP" + tab + "MDTP" + tab + "KPDTP" + endline
        print("\nMacro Name Table:")
        print(line,end="")
        self.macroNameTableFile.write(line)
        for key,value in self.macroNameTable.items():
            line = key
            for ele in value:
                line += tab + str(ele)
            line += endline
            print(line,end="")
            self.macroNameTableFile.write(line)
        self.macroNameTableFile.close()
    
    def writeParamNameTable(self):
        print("\nParameter Name Table:")
        for key,value in self.paramNameTable.items():
            line = key
            for param in value:
                line += tab + param
            line += endline
            print(line,end="")
            self.paramNameTableFile.write(line)
        self.paramNameTableFile.close()
    
    def writeMacroDefTable(self):
        print("\nMacro Definition Table:")
        counter = 1
        for value in self.macroDefTable:
            line = ""
            for item in value:
                line += item + tab
            line += endline
            print(counter,line,end="",sep="\t")
            self.macroDefTableFile.write(line)
            counter += 1
        self.macroDefTableFile.close()
            
