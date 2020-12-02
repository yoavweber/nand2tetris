import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

tree = ET.parse('xmltest.xml')
root = tree.getroot()



# creating a new element
test = ET.Element("top")
#appending it to the parsed XML 
root.append(test)

#creating a child to the new element
child = ET.SubElement(test,"child")
# # adding text to it
# child.text = 'hw?'

#insert the new element in the position
# root.insert(33,test)


# x = list(test).index(child)
# print(x)
# test = root.find()


#TODO: handle somehow with the parents element and aviod 3 arguments. the name should be "append existing element"
def appendElement(parentElement,element,appendedElement):
    elementLocation = len(list(element))
    parentElement.remove(appendedElement) 
    element.insert(elementLocation,appendedElement)
    return element
    

def getIndex(element):
    index = list(root).index(element)
    return index

def getNextElement(index):
    return root[index+1]

def compileExpression(index):
    expressionWrapper = ET.Element("expression")
    termWrapper = ET.Element("term")

    nextElement = getNextElement(index)
    if nextElement.tag != "identifier":
        print("error compiling let, missing identifier")
        return -1
    termWrapper = appendElement(root,termWrapper,nextElement)
    
    expressionWrapper.append(termWrapper)
    return expressionWrapper
    
    # previousLet = root[index+1]
    # root.remove(previousLet)
    
    
    


# ------- compiling let and sending back the element
def compileLet(index):
    letWrapper = ET.Element("letStatement")
    
    counter = index -1
    
    # #-------removing the element the let element to aviode duplication
    let = root[index]
    #-------Inserting the element again under the let wrapper
    letWrapper = appendElement(root,letWrapper,let)
    
    nextElement = getNextElement(counter)
    #TODO:create check function
    if nextElement.tag != "identifier":
        print("error compiling let, missing identifier")
        return -1
    #-------adding the first child to the let wrapper---------
    letWrapper = appendElement(root,letWrapper,nextElement)
      
    nextElement = getNextElement(counter)  
    if nextElement.text.strip() != "=":
        print("error compiling let, missing =")
        return -1
    letWrapper = appendElement(root,letWrapper,nextElement)
    
    exp = compileExpression(counter)
    letWrapper.append(exp)
    
    # nextElement = getNextElement(counter)
    
    # if nextElement.tag != "identifier":
    #     print("error compiling let, missing identifier")
    #     return -1
    # letWrapper = appendElement(root,letWrapper,nextElement)
   
    nextElement = getNextElement(counter)
    if nextElement.text.strip() != ";":
        print(nextElement.text)
        print("error compiling let, missing ; at",counter)
        return -1
    letWrapper = appendElement(root,letWrapper,nextElement)
    root.insert(index,letWrapper)
    previousLet = root[index+1]
    root.remove(previousLet)

    return letWrapper



    

    
    
x= compileLet(33)

# print(root[x].tag)
# print(root[34].tag)
        
    
    
dom = DOM.parseString(ET.tostring(root, encoding='utf8').decode('utf8'))

pretty_xml_as_string = dom.toprettyxml()



#----------------Inserting a new parents to all let------------------------
# for let in root.findall("./keyword"):
#    if(let.text.strip() == "let"):
#        letIndex = getIndex(let)
#        root.remove(let)
       
#        letWrapper = ET.Element("letStatement")
#        root.insert(letIndex,letWrapper)
#        letWrapper.insert(0,let)
#     #    alls = ET.SubElement(letWrapper,let)
#     #    root.insert(x,letWrapper)
           

# print(pretty_xml_as_string)
    
    
#---------------print the xml file
print(ET.tostring(root, encoding='utf8').decode('utf8'))