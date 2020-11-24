import classes
import sys

data = []
# with open(str(sys.argv[1])) as f:

def main():

    machineCodeArray = [] 
    with open(str(sys.argv[1])) as f:
        read_data = f.readlines()
        parser = classes.Parser(read_data)
        cleanInstructionArray = parser.parseInstructors()
        translate = classes.Translator()
        for line in cleanInstructionArray:
            machineCodeLine = translate.handleLine(line)
            machineCodeArray.append(machineCodeLine)
        infiniteLoop = '''
(INFINIELOOP)
@INFINIELOOP
0;JMP
        ''' 
        machineCodeArray.append(infiniteLoop)
        f.close()

    filename = str(sys.argv[1]).replace('vm','asm')
    print(filename,'filename')
    w = open(filename, "w")
    for command in machineCodeArray:
        print(command)
        w.write(command)  
    w.close()

main()