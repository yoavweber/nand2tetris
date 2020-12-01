import parser
import sys
import glob, os


# with open(str(sys.argv[1])) as f:
def handleString(array):
    newArray= []
    tes = []
    indices = [i for i, x in enumerate(array) if x == "\""]

    if(len(indices) %2 != 0):
        print("incomplete string")
        return -1
    if(len(indices) > 2):

        smallerIndexs1 = indices[:len(indices)//2]
        smallerIndexs2 = indices[len(indices)//2:]
        firstHandledStringArray = margeStringToList(array,smallerIndexs1)
        newArray = handleString(firstHandledStringArray) 
    else:
       newArray = margeStringToList(array,indices)
    return newArray


def margeStringToList(array,indices):
    joinString = "".join(array[indices[0]+1:indices[1]])
    stringList = array[:indices[0]]
    stringList.append(joinString)
    newArray = stringList +array[indices[1]+1:]
    return newArray
    


def main():
    fullTokenArray = ['<tokens>'] 
    
    fileArray = []
    os.chdir(str(sys.argv[1]))
    for file in glob.glob("*.jack"):
        if file == 'Main.jack':
            fileArray.insert(0,file)
        else:
            fileArray.append(file)
            
    jack = parser.JackTokenizer()
    for file in fileArray:
        with open(file) as f:
            read_data = f.readlines()
            cleaningParser = parser.Parser(read_data)
            cleanInstructionArray = cleaningParser.parseInstructors()
            for line in cleanInstructionArray:
                # we would change the state of the list later
                listLine = []
                tokenList = []
                #adding the line to the list using the advance function
                jack.advance(line,listLine)

                listLine.reverse()
                
                handleStringArray = jack.handleString(listLine)
    
                for token in handleStringArray:
                    tokenType = jack.tokenType(token)
                    if(token != " "):
                        if(tokenType == "stringConstant"):
                            fullToken = jack.tokenize(tokenType,token[1:])
                        else:
                            if(token == "<"):
                                token = "&lt;"
                            elif(token == ">"):
                                token = "&gt;"
                            elif(token == "\""):
                                token = "&quot;"
                            elif(token == "&"):
                                token = "&amp;"
                            
                            fullToken = jack.tokenize(tokenType,token)
                            
                        #create a function for all symbols
                 
                        
                        tokenList.append(fullToken)

                        f.close()
                fullTokenArray += tokenList
    fullTokenArray.append("</tokens>\n")
                
    for i in fullTokenArray:
        print(i)
            
    
    
    # jack = parser.JackTokenizer()
    # listLine = []
    # tokenList = []
    # jack.advance('do Output.printInt(sum / length);',listLine)

    # listLine.reverse()
    # handleStringArray = jack.handleString(listLine)
    
    # for token in handleStringArray:
    #     tokenType = jack.tokenType(token)
    #     print(token)
    #     if(token != " "):
    #         if(tokenType == "stringConstant"):
    #             fullToken = jack.tokenize(tokenType,token[1:])
    #         else:
    #             fullToken = jack.tokenize(tokenType,token)
    #         tokenList.append(fullToken)
    # print(tokenList)
    
        
        
    
    
    # print(handleStringArray)

    # print(fullTokenArray, "the original list(after advance and reverse")
    
#----------------------------------------------


#     machineCodeArray = [] 
#     fileArray = []
#     os.chdir(str(sys.argv[1]))
#     for file in glob.glob("*.vm"):
#         if file == 'Sys.vm':
#             fileArray.insert(0,file)
#         else:
#             fileArray.append(file)

#     for file in fileArray:
#         with open(file) as f:
#             read_data = f.readlines()
#             parser = classes.Parser(read_data)
#             cleanInstructionArray = parser.parseInstructors()
#             translate = classes.Translator()
#             for line in cleanInstructionArray:
#                 machineCodeLine = translate.handleLine(line)
#                 machineCodeArray.append(machineCodeLine)
#             f.close()

        
#     infiniteLoop = '''
# (INFINIELOOP)
# @INFINIELOOP
# 0;JMP
#     ''' 
#     machineCodeArray.append(infiniteLoop)
    
#     w = open('Sys.asm', "w")
#     for command in machineCodeArray:
#         # print(command)
#         w.write(command)  
    
#     w.close()

main()