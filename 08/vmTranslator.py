import classes
import sys
import glob, os

data = []
# with open(str(sys.argv[1])) as f:

def main():

    machineCodeArray = [] 
    fileArray = []
    os.chdir(str(sys.argv[1]))
    for file in glob.glob("*.vm"):
        if file == 'Sys.vm':
            fileArray.insert(0,file)
        else:
            fileArray.append(file)

    for file in fileArray:
        with open(file) as f:
            read_data = f.readlines()
            parser = classes.Parser(read_data)
            cleanInstructionArray = parser.parseInstructors()
            translate = classes.Translator()
            for line in cleanInstructionArray:
                machineCodeLine = translate.handleLine(line)
                machineCodeArray.append(machineCodeLine)
            f.close()

        
    infiniteLoop = '''
(INFINIELOOP)
@INFINIELOOP
0;JMP
    ''' 
    machineCodeArray.append(infiniteLoop)
    
    w = open('Sys.asm', "w")
    for command in machineCodeArray:
        # print(command)
        w.write(command)  
    
    w.close()

main()