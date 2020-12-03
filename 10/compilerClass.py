import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

_FUNCTION_TYPE = ["class", "method", "function", "constructor"]
_STATEMENTS = ["let","do","if","while","return"]


class CompliationEngine:
    
    def __init__(self,tree):
        self.tree = tree
        self.root = ET.fromstringlist(tree)
        self.newRoot = ET.Element("class")
        self.counter = 0
    
    #-----------------------Helpers-------------------------------
     #TODO: handle somehow with the parents element and aviod 3 arguments. the name should be "append existing element"
     #DEPRICATED!!!
    def __appendExistingElement(self,parentElement,element,appendedElement):
        elementLocation = len(list(element))
        parentElement.remove(appendedElement) 
        element.insert(elementLocation,appendedElement)
        return element
    
        
    def __appendElement(self,element,appendedElement):
        element.append(appendedElement)
        return element
    
    def __getIndex(self,element):
        index = list(root).index(element)
        return index
    
    def __getCurrentElement(self):
        return self.root[self.counter]

    def __getNextElement(self,index):
        return self.root[index+1]
    
    #change it to getNextElement
    def __getNextElements(self):
        self.counter += 1
        return self.root[self.counter]
    
    def __createWrapper(self,wrapperName):
       return ET.Element(wrapperName)
   
    #---------------Handle reapting tokens------------
    def __handleBrackets(self,element,brackets):
        if element.text.strip() != "{":
            print("error compiling class, expected { but recived", nextElement.text )
            return -1
        
       #trying to use this function to aviod repitation, still in test
    def __addByTag(self,tokenType,error,wrapper):
        nextElement = self.__getNextElements()
        if nextElement.tag != tokenType:
            print(error, currentElement.text,currentElement.tag)
            return -1
        
        wrapper.append(nextElement)
        
    
    
    #-------------------Program Structure----------------
    def compileClass(self,index):
        classWrapper = self.newRoot
        
        if self.root[index].text.strip() != "class":
            print("you are calling compileClass, but no class has been given")
            return -1
        
        classKeyword = self.root[index] 
        #INFO: when appending new element, the element is deleted from the main tree. therefor we can use the same index
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,classKeyword)
        classWrapper.append(classKeyword)
        
        nextElement = self.__getNextElements()
        if nextElement.tag != "identifier":
            print("error compiling class, identifier is missing")
            return -1
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,nextElement)
        classWrapper.append(nextElement)

        # nextElement = self.__getNextElement(index)
        
        nextElement = self.__getNextElements()
        if nextElement.text.strip() != "{":
            print("error compiling class, expected { but recived", nextElement.text )
            return -1
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,nextElement)
        classWrapper.append(nextElement)

        # self.newRoot.insert(0,classWrapper)
        
        # nextElement = self.__getNextElement(counter)
        nextElement = self.__getNextElements()
        while(nextElement.text.strip() == "static" or nextElement.text.strip() == "field"):
            nextElement = self.compileClassVar()
            classWrapper.append(nextElement)
            nextElement = self.__getNextElements()
        
        while(nextElement.text.strip() in _FUNCTION_TYPE):
            nextElement = self.compileSubroutine()
            classWrapper.append(nextElement)
            nextElement = self.__getNextElements()
            
        

            
        # if nextElement.text.strip() == "static" or nextElement.text.strip() == "field":
        #     nextElement = self.compileClassVar()
        # nextElement = compileClassVar(index)
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,nextElement)
        print(ET.tostring(self.newRoot, encoding='utf8').decode('utf8'))
        
        
    def compileClassVar(self):
        classVarWrapper = self.__createWrapper("classVarDec")
        
        #I am not checking to see the type of element since this is already been done by the class function
        firstElement = self.__getCurrentElement()
        classVarWrapper.append(firstElement)
        
        nextElement = self.__getNextElements()
        #checking the type of the memeber varible
        if nextElement.tag.strip() != ("keyword" or "identifier"): 
            print("error compiling classVar, expected keyword or identifier but recived", nextElement.tag, nextElement.text )
            return -1
        classVarWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        if nextElement.tag.strip() != "identifier": 
            print("error compiling classVar, expected identifier but recived", nextElement.tag, nextElement.text)
            return -1
        classVarWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        if nextElement.text.strip() != ";": 
            print("error compiling classVar, expected ; but recived", nextElement.text )
            return -1
        classVarWrapper.append(nextElement)
        
        return classVarWrapper
    
    
    def compileSubroutine(self):
        
        subRoutineWrapper = self.__createWrapper("subroutineDec")
        
        #I am not checking to see the type of element since this is already been done by the class function
        firstElement = self.__getCurrentElement()
        subRoutineWrapper.append(firstElement)
        nextElement = self.__getNextElements()
        #checking what type is the function(currently types are not being handled)
        if nextElement.tag.strip() != ("keyword" or "identifier"): 
            print("error compiling classVar, expected keyword or identifier but recived", nextElement.tag, nextElement.text )
            return -1
        subRoutineWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        if nextElement.tag.strip() != "identifier": 
            print("error compiling classVar, expected identifier but recived", nextElement.tag, nextElement.text)
            return -1
        subRoutineWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        if nextElement.text.strip() != "(": 
            print("error compiling classVar, expected ; but recived", nextElement.text )
            return -1 
        subRoutineWrapper.append(nextElement)
        
        #if next elements are the argumenst of the function arguments
        nextElement = self.__getNextElements()
        if nextElement.text.strip() == ")":
            parameterListWrapper = self.__createWrapper("parameterList")
            parameterListWrapper.text = ' '
            subRoutineWrapper.append(parameterListWrapper)
            subRoutineWrapper.append(nextElement)
        elif(nextElement.tag == ("keyword" or "identifier")):
            nextElement = self.compileParameterList()
            subRoutineWrapper.append(nextElement)
            #appanding the next element which is ")"
            nextElement = self.__getCurrentElement()
            subRoutineWrapper.append(nextElement)
        else:
            print("error compiling subRoutin, expected ) but recived", nextElement.text )
            return -1 
        
        nextElement = self.__getNextElements()
        
        nextElement = self.compileSubroutineBody()
        subRoutineWrapper.append(nextElement)
            
        return subRoutineWrapper

    
    def compileParameterList(self):
        parameterListWrapper = self.__createWrapper("parameterList")
        nextElement = self.__getCurrentElement()
        while(nextElement.text.strip() != ")"):
            if nextElement.tag != ("keyword" or "identifier"):
                print("error compiling compileParameterList, expected keyword or identifier but recived", nextElement.text )
                return -1  
            parameterListWrapper.append(nextElement)
            
            nextElement = self.__getNextElements()
            if nextElement.tag != ("keyword" or "identifier"):
                print("error compiling compileParameterList, expected keyword or identifier but recived", nextElement.text )
                return -1  
            parameterListWrapper.append(nextElement)
            
            nextElement = self.__getNextElements()
            if nextElement.text.strip() == ",":
                parameterListWrapper.append(nextElement)
            elif(nextElement.text.strip() == ")"):
                break
            else:
                print("error compiling compileParameterList, expected , but recived", nextElement.text,nextElement.text )
                return -1  
            
            nextElement = self.__getNextElements()
        
        return parameterListWrapper
        
        
    def compileSubroutineBody(self):
        subroutineBodyWrapper = self.__createWrapper("subroutineBody")
        nextElement = self.__getCurrentElement()
        if self.__handleBrackets(nextElement,"{") == -1:
            return -1
        subroutineBodyWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        
        if nextElement.text.strip() == "var":
            while(nextElement.text.strip() == "var"):
                nextElement = self.compileVar()
                subroutineBodyWrapper.append(nextElement)
                
                nextElement = self.__getNextElements()
        # nextElement = self.handleStatments("let")
        
        return subroutineBodyWrapper
            
            
    def compileVar(self):
        varWrapper = self.__createWrapper("varDec")
        currentElement = self.__getCurrentElement()
        if currentElement.text.strip() != "var":
            print("no 'var' was found, got: ", currentElement.text,currentElement.tag)
            return -1
        varWrapper.append(currentElement)
        
        # nextElement = self.__getNextElements()
        # if nextElement.tag != "keyword":
        #     print("no keyword type was found, got: ", nextElement.text,nextElement.tag)
        #     return -1
        # varWrapper.append(nextElement)
        
        nextElement = self.__getNextElements()
        if nextElement.tag != ("identifier" or "keyword"):
            print("no keyword or identifier type was found, got: ", currentElement.text,currentElement.tag)
            return -1
        varWrapper.append(nextElement)
        
        tokenType = "identifier"
        error = "no identifier type was found, got: "
        self.__addByTag(tokenType,error,varWrapper)
        
        nextElement = self.__getNextElements()
        while(nextElement.text.strip() != ";"):
            if nextElement.text.strip() != ",":
                print("missing ',', got: ", currentElement.text,currentElement.tag)
                return -1
            varWrapper.append(nextElement)
            
            tokenType = "identifier"
            error = "no identifier type was found, got: "
            self.__addByTag(tokenType,error,varWrapper)
            
            nextElement = self.__getNextElements()
            
        return varWrapper
            
       
        
            
            
            
     
            
            
        
        
        
            
    

                    
        
        
        
    #-------------------statments--------------------------
    
    def handleStatments(self,statment):
        myDict = {"let":self.compileLet,"do":self.compileDo,"if":self.compileIf,"while":self.compileWhile,"return":self.compileReturn }
        return myDict[statment]()
            
            
    def compileDo(self):
        return -1
    
    def compileIf(self):
        return -1
    
    def compileWhile(self):
        return -1
    
    def compileReturn(self):
        return -1
    
    def compileLet(self):

        letWrapper = ET.Element("letStatement") 
        
        counter = index -1
        
        # #-------removing the element the let element to aviode duplication
        let = root[index]
        #-------Inserting the element again under the let wrapper
        letWrapper = __appendExistingElement(root,letWrapper,let)
        
        nextElement = __getNextElement(counter)
        #TODO:create check function
        if nextElement.tag != "identifier":
            print("error compiling let, missing identifier")
            return -1
        #-------adding the first child to the let wrapper---------
        letWrapper = __appendExistingElement(root,letWrapper,nextElement)
        
        nextElement = __getNextElement(counter)  
        if nextElement.text.strip() != "=":
            print("error compiling let, missing =")
            return -1
        letWrapper = __appendExistingElement(root,letWrapper,nextElement)
        
        exp = compileExpression(counter)
        letWrapper.append(exp)
    
        nextElement = __getNextElement(counter)
        if nextElement.text.strip() != ";":
            print(nextElement.text)
            print("error compiling let, missing ; at",counter)
            return -1
        letWrapper = __appendExistingElement(root,letWrapper,nextElement)
        root.insert(index,letWrapper)
        previousLet = root[index+1]
        root.remove(previousLet)

        return letWrapper
    
    #-------------------expersions--------------------------
    def compileExpression(index):
        expressionWrapper = ET.Element("expression")
        termWrapper = ET.Element("term")

        nextElement = __getNextElement(index)
        if nextElement.tag != "identifier":
            print("error compiling let, missing identifier")
            return -1
        termWrapper = __appendExistingElement(root,termWrapper,nextElement)
        
        expressionWrapper.append(termWrapper)
        return expressionWrapper


   
    
    