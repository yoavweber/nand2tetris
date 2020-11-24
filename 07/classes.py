import random
import string
import sys

class Parser:
    def __init__(self,data):
        self.data = data
    
    def __removeCommentsAndWhiteSpace(self,line):
        noComments = line.split('/')[0]
        noWhiteSpace = noComments.split('\n')[0]
        return noWhiteSpace

    def parseInstructors(self):
        instructors = []
        for line in self.data:
            noCommentsLine = self.__removeCommentsAndWhiteSpace(line)
            if noCommentsLine:
                instructors.append(noCommentsLine)
        return instructors


class Translator:
    
    def handleLine(self,command):
        commandWord = command.split(" ")
        if commandWord[0] == 'push' or commandWord[0] == 'pop':
            if commandWord[1] == 'constant':
                machineCommand = self.__pushConstant(commandWord[2])
                return machineCommand
            elif commandWord[1] == 'argument':
                machineCommand = self.__segment(commandWord[0],commandWord[2],'ARG')
                return machineCommand
            elif commandWord[1] == 'this':
                machineCommand = self.__segment(commandWord[0],commandWord[2],'THIS')
                return machineCommand
            elif commandWord[1] == 'that':
                machineCommand = self.__segment(commandWord[0],commandWord[2],'THAT')
                return machineCommand
            elif commandWord[1] == 'local':
                machineCommand = self.__segment(commandWord[0],commandWord[2],'LCL')
                return machineCommand
            elif commandWord[1] == 'temp':
                segmentLocation = self.__tempLocation(commandWord[2])
                machineCommand = self.__temp(commandWord[0],segmentLocation)  
                return machineCommand
            elif commandWord[1] == 'pointer':
                segmentType = self.__pointerSegment(commandWord[2])
                machineCommand = self.__temp(commandWord[0],segmentType)
                return machineCommand
            elif commandWord[1] == 'static':
                filename = self.getVMfileName() + f'{commandWord[2]}'
                machineCommand = self.__temp(commandWord[0],filename)
                return machineCommand
        # if commandWord[0] == 'pop':
        #     if commandWord[1] == 'argument':
        #         machineCommand = self.__segment(commandWord[0],commandWord[2],'ARG')
        #         return machineCommand
        #     elif commandWord[1] == 'this':
        #         machineCommand = self.__segment(commandWord[0],commandWord[2],'THIS')
        #         return machineCommand
        #     elif commandWord[1] == 'that':
        #         machineCommand = self.__segment(commandWord[0],commandWord[2],'THAT')
        #         return machineCommand
        #     elif commandWord[1] == 'local':
        #         machineCommand = self.__segment(commandWord[0],commandWord[2],'LCL')
        #         return machineCommand
        #     elif commandWord[1] == 'temp':
        #         segmentLocation = self.__tempLocation(commandWord[2])
        #         machineCommand = self.__temp(commandWord[0],segmentLocation)
        #         return machineCommand
        #     elif commandWord[1] == 'pointer':
        #         segmentType = self.__pointerSegment(commandWord[2])
        #         machineCommand = self.__temp(commandWord[0],segmentType)
        #         return machineCommand
        #     elif commandWord[1] == 'static':
        #         filename = self.getVMfileName() + f'{commandWord[2]}'
        #         machineCommand = self.__temp(commandWord[0],filename)
        #         return machineCommand




        elif commandWord[0] == 'add':
            machineCommand = self.__add()
            return machineCommand
        elif commandWord[0] == 'sub':
            return self.__sub()
        elif commandWord[0] == 'eq':
            return self.__equalTo()
        elif commandWord[0] == 'lt':
            return self.__lesserThan()
        elif commandWord[0] == 'gt':
            return self.__greaterThan()
        elif commandWord[0] == 'or':
            return self.__or()
        elif commandWord[0] == 'and':
            return self.__and()
        elif commandWord[0] == 'neg':
            return self.__neg()
        elif commandWord[0] == 'not':
            return self.__not()
        else:
            print('unknown command')


#-------------utils----------------
    def get_random_string(self,length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def __stackOperation(self,operation):
        if operation == "pop":
            machineCommand = '''

@SP
A=M
A=A-1
D=M
@SP
M=M-1
'''
        else:
            machineCommand = '''
@SP
A=M
M=D
//assign the stack pzointer to the new location
@SP
M=M+1
'''
        return machineCommand

    def getVMfileName(self):
        filename =  str(sys.argv[1])[26:-2]
        print(filename)
        return filename

#------------------Arithmic Commands----------------------
    def __arithmicCommand(self,operation):
        command = f'''
@SP
A=M
A=A-1
D=M
A=A-1
{operation}
@SP
M=M-1
        '''
        return command

    def __add(self):
        command = 'M=D+M'
        fullCommend = '''
// add''' + self.__arithmicCommand(command)
        return fullCommend

    def __sub(self):
        command = '''
D=-D
M=D+M
        '''
        fullCommend = '''
// sub''' + self.__arithmicCommand(command)
        return fullCommend
        return fullCommend


    def __or(self):
        command = 'M=D|M'
        fullCommend = '''
// or''' + self.__arithmicCommand(command)
        return fullCommend

    def __and(self):
        command = 'M=D&M'
        fullCommend = '''
// or''' + self.__arithmicCommand(command)
        return fullCommend


        

#------------Boolean commands---------------------------------------------
    def __boolCommand(self,operation):
        operationRandom = self.get_random_string(10)
        infinityRandom = self.get_random_string(10)
        command = f'''
@SP
M=M-1
A=M
D=M
A=A-1
D=D-M
@{operationRandom}
D;{operation}
@SP
A=M-1
M=0
@{infinityRandom}
D;JMP
({operationRandom})
@SP
A=M-1
M=-1
({infinityRandom})
'''
        return command

    def __equalTo(self):
        command = 'JEQ'
        fullCommend = '''
// eq''' + self.__boolCommand(command)
        return fullCommend

    def __greaterThan(self):
        command = 'JLT'
        fullCommend = '''
// gt''' + self.__boolCommand(command)
        return fullCommend

    def __lesserThan(self):
        command = 'JGT'
        fullCommend = '''
// lt''' + self.__boolCommand(command)
        return fullCommend

#------------single commands, oprate on the latest item on the stack-------
    def __singleCommand(self,operation):
        command=f'''
@SP
A=M
A=A-1
{operation}
    '''
        return command

    def __neg(self):
        command = 'M=-M'
        fullCommend = '''
// neg''' + self.__singleCommand(command)
        return fullCommend

    def __not(self):
        command = 'M=!M'
        fullCommend = '''
// not''' + self.__singleCommand(command)
        return fullCommend

#---------------- Stack Operations--------------------
    def __pushConstant(self,number):
        command =  f'''
// push constant {number}
@{number}
D=A
@SP
A=M
M=D
@SP
M=M+1
        '''
        return command
#-------------Memory command ---------------------
    def __popCommand(self,segment,location):
        varRandom = self.get_random_string(10)
        command = f'''
@{location}
D=A
@{segment}
A=M+D
D=A
@{varRandom}
//get the last value in the stack and assign the stack pointer to the right location
M=D
{self.__stackOperation('pop')}
//store it in the segment
@{varRandom}
A=M
M=D
            '''
        return command

    def __pushCommand(self,segment,location):
        command = f'''
@{location}
D=A
@{segment}
A=M+D
D=M
//get the last value in the stack 
{self.__stackOperation('push')}
            '''
        return command
#TODO delete this functuin
    def __argument(self,stackOperation,location):
        segment = 'ARG'
        if stackOperation == 'pop':
            segmentCommand = self.__popCommand(segment,location)
        else:
            segmentCommand = self.__pushCommand(segment,location)
        fullCommend = f'''
// {stackOperation} argument {location}''' + segmentCommand
        return fullCommend
        
    def __tempLocation(self,location):
        location = 5 + int(location)
        return str(location)

    def __temp(self,stackOperation,location):
        if stackOperation == 'pop':
            command = f'''
// pop temp {location}
{self.__stackOperation('pop')}
@{location}
M=D
'''
        else:
            command = f'''
// push temp {location}
@{location}
D=M
{self.__stackOperation('push')}
'''
        return command

    def __pointerSegment(self,stackOperation):
        if stackOperation == '0':
            return 'THIS'
        else:
            return 'THAT'

    def __segment(self,stackOperation,location,segmentType):
        segment = segmentType
        if stackOperation == 'pop':
            segmentCommand = self.__popCommand(segment,location)
        else:
            segmentCommand = self.__pushCommand(segment,location)
        fullCommend = f'''
// {stackOperation} {segmentType} {location}''' + segmentCommand
        return fullCommend




    
