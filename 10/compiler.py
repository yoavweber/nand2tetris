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
    jack = parser.JackTokenizer()
    listLine = []
    tokenList = []
    # jack.advance('let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: ");',listLine)
    jack.advance('let length = Keyboard.readInt("HOW MANY NUMBERS? ");, "sa d";',listLine)

    listLine.reverse()
    handleStringArray = jack.handleString(listLine)
    
    # for s in handleStringArray:
        
    
    print(handleStringArray)
    print(listLine, "the original list(after advance and reverse")
    


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