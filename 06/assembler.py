import values
import sys

def checkIntructType(symbol):
    if(symbol[0] == "@"):
        return "A"
    # elif(symbol[0] == "(" and symbol[-1] == ")"):
    #     return 'lableSymbol'
    return "C"

def assignLable(array):
    newArray = []
    counter = 0
    for c in array:
        if(c[0] == "(" and c[-1] == ")"):
            commandLocation = counter
            values.symbols[f'{c[1:-1]}'] = commandLocation
        else:
            newArray.append(c)
            counter += 1
    return newArray


def convertToBinary(num):
    binary = ''
    while num != 0:
        if num%2 == 1:
            prevBinary = binary
            binary = '1' + prevBinary
        else:
            prevBinary = binary
            binary = '0' + prevBinary
        num = num // 2

    zeroAmount = 16 - len(binary)
    binaryNum = ("0" * zeroAmount) + binary 
    return binaryNum


def handleAinstruct(s):
    try:
        intNum = int(s[1:])
    except ValueError:
        symbolValue = symbolsHandler(s[1:])
        address = convertToBinary(symbolValue)
    else:
        address = convertToBinary(intNum)
    return f'{address}'



def symbolsHandler(symbol):
    dic = values.symbols
    if symbol in dic:
        return dic[symbol] # the a instuction location
    else:
       return handleVaribles(symbol)

def handleVaribles(symbol):
    dic = values.symbols
    currentMemoryLocation = values.memoryLocation
    dic[symbol] = currentMemoryLocation
    values.memoryLocation += 1
    return currentMemoryLocation


def handleCinstruct(command):
    destIndex = command.find("=")
    jumpIndex = command.find(";")
    #Add error handling here
    if destIndex == -1:
        destSymbol = ""
        destIndex = 0
    else:
        destSymbol = command[:destIndex]
        destIndex = destIndex + 1
    if jumpIndex == -1:
        jumpSymbol = ""
        jumpIndex = len(command) + 1
    else:
        jumpSymbol = command[jumpIndex+1:]

    compSymbol = command[destIndex:jumpIndex]

    dest = values.cInstructorsDest[destSymbol]
    comp = values.cInstructorsComp[compSymbol]
    jump = values.cInstructorsJump[jumpSymbol]
    instructions = '111' + comp + dest + jump
    return instructions



def main():
    rawCommands = []
    commands = []
    binaryCommends = []
    with open(str(sys.argv[1])) as f:
        
        read_data = f.readline()
        for line in f:
            command = ''
            for s in line:
                command += s
            rawCommands.append(command)
        f.close()

    for command in rawCommands:
        comments= command.find("//")
        if comments != -1:
            if command[:comments] != '':
                commands.append(command[:comments].strip())
                
        elif(command != "\n" ):
            commands.append(command[0:-1].strip())

    
    filename = str(sys.argv[1]).replace('asm','hack')
    w = open(filename, "w")
    
    commendCounter = 0
    print(commands)
    finalCommends = assignLable(commands)
    for command in finalCommends:
        intructType = checkIntructType(command)
        if intructType == 'A':
            aInstruction = handleAinstruct(command)
            commendCounter += 1
            w.write(aInstruction+'\n')  

        else:
            cInstruction = handleCinstruct(command)
            commendCounter += 1
            w.write(cInstruction+'\n')
    w.close()

    print(binaryCommends)
    print(values.symbols)  


    
main()



