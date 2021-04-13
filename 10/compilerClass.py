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
    
    def __printTree(self,element):
        print(ET.tostring(element, encoding='utf8').decode('utf8'))


    # def __getNextElement(self,index):
    #     return self.root[index+1]
    
    #change it to getNextElement
    def __getNextElement(self):
        self.counter += 1
        return self.root[self.counter]
    
    def __createWrapper(self,wrapperName):
       return ET.Element(wrapperName)
   
    #---------------Handle reapting tokens(components)------------
    def __handleBrackets(self,element,brackets):
        if element.text.strip() != "{":
            print("error compiling class, expected { but recived", nextElement.text )
            return -1
        
       #trying to use this function to aviod repitation, still in test
    def __addByTag(self,tokenType,error,wrapper):
        nextElement = self.__getNextElement()
        if nextElement.tag != tokenType:
            print(error, currentElement.text,currentElement.tag)
            return -1
        
        wrapper.append(nextElement)
        
    def __addKeywordAndIdentifier(self,wrappingElement):
        nextElement = self.__getCurrentElement()
        #checking the type of the memeber varible
        if nextElement.tag.strip() != "keyword": 
            print("error compiling classVar, expected keyword or identifier but recived", nextElement.tag, nextElement.text )
            return -1
        wrappingElement.append(nextElement)
        
        nextElement = self.__getNextElement()
        if nextElement.tag.strip() != "identifier": 
            print("error compiling classVar, expected identifier but recived", nextElement.tag, nextElement.text)
            return -1
        wrappingElement.append(nextElement)
        
        return self.__getNextElement()
    
    def __errorMessage(self,error,element,extra=""):
        print(f"exected to find {error}, got: ", element.text ,element.tag)
        
        
    
    
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
        
        nextElement = self.__getNextElement()
        if nextElement.tag != "identifier":
            print("error compiling class, identifier is missing")
            return -1
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,nextElement)
        classWrapper.append(nextElement)

        # nextElement = self.__getNextElement(index)
        
        nextElement = self.__getNextElement()
        if nextElement.text.strip() != "{":
            print("error compiling class, expected { but recived", nextElement.text )
            return -1
        # classWrapper = self.__appendExistingElement(self.root,classWrapper,nextElement)
        classWrapper.append(nextElement)

        # self.newRoot.insert(0,classWrapper)
        
        # nextElement = self.__getNextElement(counter)
        nextElement = self.__getNextElement()
        while(nextElement.text.strip() == "static" or nextElement.text.strip() == "field"):
            nextElement = self.compileClassVar()
            classWrapper.append(nextElement)
            nextElement = self.__getNextElement()
        
        while(nextElement.text.strip() in _FUNCTION_TYPE):
            nextElement = self.compileSubroutineDec()
            classWrapper.append(nextElement)
            nextElement = self.__getNextElement()
            
        

            
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
        
        nextElement = self.__getNextElement()
        #checking the type of the memeber varible
        if nextElement.tag.strip() != ("keyword" or "identifier"): 
            print("error compiling classVar, expected keyword or identifier but recived", nextElement.tag, nextElement.text )
            return -1
        classVarWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        if nextElement.tag.strip() != "identifier": 
            print("error compiling classVar, expected identifier but recived", nextElement.tag, nextElement.text)
            return -1
        classVarWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        if nextElement.text.strip() != ";": 
            print("error compiling classVar, expected ; but recived", nextElement.text )
            return -1
        classVarWrapper.append(nextElement)
        
        return classVarWrapper
    
    
    def compileSubroutineDec(self):
        
        subRoutineWrapper = self.__createWrapper("subroutineDec")
        
        #I am not checking to see the type of element since this is already been done by the class function
        firstElement = self.__getCurrentElement()
        subRoutineWrapper.append(firstElement)
        nextElement = self.__getNextElement()
        #checking what type is the function(currently types are not being handled)
        if nextElement.tag.strip() != ("keyword" or "identifier"): 
            print("error compiling classVar, expected keyword or identifier but recived", nextElement.tag, nextElement.text )
            return -1
        subRoutineWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        if nextElement.tag.strip() != "identifier": 
            print("error compiling classVar, expected identifier but recived", nextElement.tag, nextElement.text)
            return -1
        subRoutineWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        if nextElement.text.strip() != "(": 
            print("error compiling classVar, expected ; but recived", nextElement.text )
            return -1 
        subRoutineWrapper.append(nextElement)
        
        #if next elements are the argumenst of the function arguments
        nextElement = self.__getNextElement()
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
        
        nextElement = self.__getNextElement()
        
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
            
            nextElement = self.__getNextElement()
            if nextElement.tag != ("keyword" or "identifier"):
                print("error compiling compileParameterList, expected keyword or identifier but recived", nextElement.text )
                return -1  
            parameterListWrapper.append(nextElement)
            
            nextElement = self.__getNextElement()
            if nextElement.text.strip() == ",":
                parameterListWrapper.append(nextElement)
            elif(nextElement.text.strip() == ")"):
                break
            else:
                print("error compiling compileParameterList, expected , but recived", nextElement.text,nextElement.text )
                return -1  
            
            nextElement = self.__getNextElement()
        
        return parameterListWrapper
        
        
    def compileSubroutineBody(self):
        subroutineBodyWrapper = self.__createWrapper("subroutineBody")
        nextElement = self.__getCurrentElement()
        if self.__handleBrackets(nextElement,"{") == -1:
            return -1
        subroutineBodyWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        
        if nextElement.text.strip() == "var":
            while(nextElement.text.strip() == "var"):
                nextElement = self.compileVar()
                subroutineBodyWrapper.append(nextElement)
                
                nextElement = self.__getNextElement()
       
        #changing the next element to next statment to make the code more readble
        nextStatment = nextElement
        while nextStatment.text.strip() != '}':
            nextStatment = self.compileStatments()
            subroutineBodyWrapper.append(nextElement)
            nextStatment = self.__getNextElement()
            
            
        return subroutineBodyWrapper
            
            
    def compileVar(self):
        varWrapper = self.__createWrapper("varDec")
        currentElement = self.__getCurrentElement()
        if currentElement.text.strip() != "var":
            print("no 'var' was found, got: ", currentElement.text,currentElement.tag)
            return -1
        varWrapper.append(currentElement)
        
        # nextElement = self.__getNextElement()
        # if nextElement.tag != "keyword":
        #     print("no keyword type was found, got: ", nextElement.text,nextElement.tag)
        #     return -1
        # varWrapper.append(nextElement)
        
        nextElement = self.__getNextElement()
        
        if nextElement.tag == "identifier" or  nextElement.tag == "keyword":
            varWrapper.append(nextElement)
        else:
            print("no keyword or identifier type was found, got: ", currentElement.text,currentElement.tag)
            return -1    
            
        tokenType = "identifier"
        error = "no identifier type was found, got: "
        self.__addByTag(tokenType,error,varWrapper)
        
        nextElement = self.__getNextElement()
        while(nextElement.text.strip() != ";"):
            if nextElement.text.strip() != ",":
                print("missing ',', got: ", currentElement.text,currentElement.tag)
                return -1
            varWrapper.append(nextElement)
            
            tokenType = "identifier"
            error = "no identifier type was found, got: "
            self.__addByTag(tokenType,error,varWrapper)
            
            nextElement = self.__getNextElement()
        
        #appanding the last element of the var, which is ;
        varWrapper.append(nextElement)
            
        return varWrapper
        
    def compileStatments(self):
        statmentWrapper = self.__createWrapper("statements")
        currentElement = self.__getCurrentElement()
        try:
            statment = self.handleStatments(currentElement.text.strip())
            statmentWrapper.append(statment)
        except KeyError:
            print("!!!")

        return statmentWrapper
            
            
       
        
            
            
            
             
        
    #-------------------statments--------------------------
    
    def handleStatments(self,statment):
        myDict = {"let":self.compileLet,"do":self.compileDo,"if":self.compileIf,"while":self.compileWhile,"return":self.compileReturn }
        return myDict[statment]()
            
            
    def compileDo(self):
        doWrapper = ET.Element("doStatement") 
        nextElement = self.__addKeywordAndIdentifier(doWrapper)
        
        while(nextElement.text.strip() != "("):
            if nextElement.text.strip() != ".":
                print("expected an . recived: ", nextElement.text,nextElement.tag)
                return - 1
            doWrapper.append(nextElement)
            
            nextElement = self.__getNextElement()
            if nextElement.tag != "identifier":
                print("expected an idenrifier, recived:", nextElement.text,nextElement.tag)
                return -1
            doWrapper.append(nextElement)
            nextElement = self.__getNextElement()
        #adding the ( after checking the while statment
        doWrapper.append(nextElement)
        
        
        closingBrackets = self.__getNextElement()
        if closingBrackets.text.strip() != ")":
            closingBrackets= self.compileExpressionList
        doWrapper.append(closingBrackets)
        
        closingStatment = self.__getNextElement()
        if closingStatment.text.strip() != ";":
            print("expected ;, recived:", nextElement.text,nextElement.tag)
            return -1
        doWrapper.append(closingStatment)
        

        return doWrapper
    
    def compileIf(self):
        ifWrapper = ET.Element("ifStatement")
        
        ifElement = self.__getCurrentElement()
        if ifElement.text.strip() != "if":
            self.__errorMessage("if",ifElement)
            return -1
        ifWrapper.append(ifElement)
        
        openBrackets = self.__getNextElement()
        if openBrackets.text.strip() != "(":
            self.__errorMessage("(",ifElement)
            return -1
        ifWrapper.append(openBrackets)
        
        self.__getNextElement()
        expression = self.compileExpression()
        ifWrapper.append(expression)
        
        closeBrackets = self.__getNextElement()
        if closeBrackets.text.strip() != ")":
            self.__errorMessage(")",closeBrackets)
            return -1
        ifWrapper.append(closeBrackets)
        
        openCurrlyBrackets = self.__getNextElement()
        if openCurrlyBrackets.text.strip() != "{":
            self.__errorMessage("{",openCurrlyBrackets)
            return -1
        ifWrapper.append(openCurrlyBrackets)
        
        nextStatment = self.__getNextElement()
        #TODO: repeating few times, create a function to handle it
        while(nextStatment.text.strip() != "}"):
            nextStatment = self.compileStatments()
            ifWrapper.append(nextStatment)
            nextStatment = self.__getNextElement()
        ifWrapper.append(nextStatment)
        
        elseOrEnd = self.__getNextElement()
        if elseOrEnd.text.strip() != "else":
            return ifWrapper
        else:
            ifWrapper.append(elseOrEnd)
            openCurrlyBrackets = self.__getNextElement()
            if openCurrlyBrackets.text.strip() != "{":
                self.__errorMessage("{",openCurrlyBrackets)
                return -1
            while(nextStatment.text.strip() != "}"):
                nextStatment = self.compileStatments()
                ifWrapper.append(nextStatment)
                nextStatment = self.__getNextElement()
            ifWrapper.append(nextStatment)
            return ifWrapper
                
    def compileWhile(self):
        print("from while")
        return -1
    
    def compileReturn(self):
        returnWrapper = ET.Element("returnStatement")
        returnItem = self.__getCurrentElement()
        
        if returnItem.text.strip() != "return":
            self.__errorMessage("return",returnItem)
            return -1
        returnWrapper.append(returnItem)
        
        endingLine = self.__getNextElement()
        if endingLine.text.strip() != ";":
            self.__errorMessage(";",endingLine)
            return -1
        returnWrapper.append(endingLine)
        
        return returnWrapper
    
    def compileLet(self):
        letWrapper = ET.Element("letStatement") 
                
        # #-------removing the element the let element to aviode duplication
        letElement = self.__getCurrentElement()

        if letElement.text.strip() != "let":
            print("error compiling let, missing keyword let, got instead:",letElement.text,letElement.tag)
            return -1
        letWrapper.append(letElement)
        
        
        identifier = self.__getNextElement()
        #TODO:create check function
        if identifier.tag != "identifier":
            self.__errorMessage("identifier",identifier)
            return -1
        #-------adding the first child to the let wrapper---------
        letWrapper.append(identifier)
        
        equalOrExpression = self.__getNextElement()  
        
        if equalOrExpression.text.strip() == "[":
            letWrapper.append(equalOrExpression)
            self.__getNextElement()
            exp = self.compileExpression()
            letWrapper.append(exp)
            
            closingSquareBrackets = self.__getNextElement()
            if closingSquareBrackets.text.strip() != "]":
                self.__errorMessage("]",closingBrackets)
                return -1
            letWrapper.append(closingSquareBrackets)
            
            equalOrExpression = self.__getNextElement()
             
        if equalOrExpression.text.strip() != "=":
            self.__errorMessage("=",equalOrExpression)
            return -1
        letWrapper.append(equalOrExpression)
        
        nextElement = self.__getNextElement()
        exp = self.compileExpression()
        letWrapper.append(exp)
    
        endElement = self.__getNextElement()
        if endElement.text.strip() != ";":
            self.__errorMessage(";",endElement)
            return -1
        letWrapper.append(endElement)
        return letWrapper
    
    #-------------------expersions--------------------------
    def compileExpression(self):
        expressionWrapper = ET.Element("expression")
        termWrapper = ET.Element("term")
        

        currentElement = self.__getCurrentElement()
        if currentElement.tag != "identifier":
            self.__errorMessage("identifier",currentElement)
            return -1
        termWrapper.append(currentElement)
                
        expressionWrapper.append(termWrapper)
        return expressionWrapper
    
    def compileTerm(self):
        #term is every part of the expression after the =
        termWrapper = ET.Element("term")
        currentElement = self.__getCurrentElement()
        if currentElement.tag != "identifier":
            self.__errorMessage("identifier",currentElement)
            return -1
        termWrapper.append(currentElement)
        


    def compileExpressionList(self):
        expressionListWrapper = ET.Element("expressionList")
        currentElement = self.__getCurrentElement()
        
        if currentElement.text.strip() == ")":
            expressionListWrapper.append(currentElement)
        else:
            #TODO: handle expression correctly
            print("handling exeprssion")
            exeprssion = self.compileExpression()
            expressionListWrapper.append(exeprssion)
            
        
        return compileExpressionList
    
    