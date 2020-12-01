import random
import string
import sys

from tokenTypes import (KEYWORD, SYMBOL, STRING, INTEGER, IDENTIFIER)


_KEYWORDS = ["class", "method", "function", "constructor", "int", "boolean",
             "char", "void", "var", "static", "field", "let", "do", "if",
             "else", "while", "return", "true", "false", "null", "this"]

_SYMBOLS = ["{", "}", "[", "]", "(", ")", ".", ",", ";", "+", "-", "*", "/",
            "&", "|", "<", ">", "=", "~"]


class Parser:
    def __init__(self,data):
        self.data = data
    
    def __removeCommentsAndWhiteSpace(self,line):
        line = line.split('//')[0]
        line = line.split('/**')[0]
        line = line.split('*/')[0]
        try:
            if line[0] == '*':
                line = line.split('*')[0]
        except IndexError:
            pass
        noWhiteSpace = line.split('\n')[0]
        return noWhiteSpace

    def parseInstructors(self):
        instructors = []
        for line in self.data:
            line = line.strip()
            
            noCommentsLine = self.__removeCommentsAndWhiteSpace(line)
            # print(noCommentsLine)
            # try:
            #     if noCommentsLine[0] == "*" or noCommentsLine[0] == "\*":
            #         continue
            # except IndexError:
                
            if noCommentsLine:
                instructors.append(noCommentsLine.strip())
        return instructors

    def getVMfileName(self):
        filename =  str(sys.argv[1])[26:-2]
        return filename


class JackTokenizer:

    
    def tokenize(self,token, word):
        token = f'''<{token}> {word} </{token}>'''
        return token

    
    #currently reciving a line(need to be trimmed before)
    def advance(self,word,listLine):
        token = ''
        counter = 0
        for s in word:
            if(self.__hasMoreTokens(s)):
                token += s
                counter += 1
            else:
                
                # The string is ended and therefor return the last token
                try:
                    splitWord = word[counter:]
                except IndexError:
                    listLine.append(token)
                    return token
                else:
                    if(token == ''):
                        token += s
                        otherSplitWord = word[counter+1:]
                        self.advance(otherSplitWord,listLine)
                        # if(token != ' '):
                        listLine.append(token)
                        return token
                    else:
                       
                        self.advance(splitWord,listLine)
                        listLine.append(token)
                        return token

        if(token != ''):
            listLine.append(token)
        return token

    #should parse each word in the line(maybe each letter and not word)
    def __hasMoreTokens(self,nextWord):
        if(nextWord.isalnum() or nextWord == "_"):
            return True
        else:
            return False
        
        


        
    
    def stringVal(word):
       if word[0] == "\"":
           nextWord = advance(word) 
           string = ""
           while(nextWord != "\""):
               string += nextWord
               nextWord = advance(nextWord) 
           return string

    def handleString(self,array):
        newArray= []
        tes = []
        indices = [i for i, x in enumerate(array) if x == "\""]

        if(len(indices) %2 != 0):
            print("incomplete string")
            return -1
        
        if len(indices) == 0:
            return array
        
        if(len(indices) > 2):
            smallerIndexs1 = indices[:len(indices)//2]
            smallerIndexs2 = indices[len(indices)//2:]
            firstHandledStringArray = self.__margeStringToList(array,smallerIndexs1)
            newArray = self.handleString(firstHandledStringArray) 
        else:
            newArray = self.__margeStringToList(array,indices)
        return newArray
    
    def __margeStringToList(self,array,indices):
        
        #adding \" so the token type could identify the string
        joinString = "\"" +"".join(array[indices[0]+1:indices[1]])
        stringList = array[:indices[0]]
        stringList.append(joinString)
        newArray = stringList +array[indices[1]+1:]
        return newArray
    
    # def isIdentifier(word):
    #     if word[0].isnumeric():
    #         return False
    #     for s in word:
    #         if(s.isalnum() or s == "_" ):


    def tokenType(self,token):
        if(token in _KEYWORDS):
            return KEYWORD
        elif(token in _SYMBOLS):
            return SYMBOL
        elif(token.isnumeric() and int(token) < 32767):
            return INTEGER
        elif(token[0] == "\"" or token[0] == "\'"):
            return STRING
        else:
            return  IDENTIFIER
            
