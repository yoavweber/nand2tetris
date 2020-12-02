import xml.etree.ElementTree as ET



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


def getIndex(element):
    index = list(root).index(element)
    return index

def getNextElement(index):
    return root[index+1]


def compileLet(index):
    letWrapper = ET.Element("letStatement")
    childCounter = 0
    counter = index
    
    # #-------removing the element the let element to aviode duplication
    let = root[index]
    # root.remove(let)
    
    #-------Inserting the element again under the let wrapper
    letWrapper.insert(childCounter,let)
    childCounter += 1
    
    nextElement = getNextElement(index)
    #TODO:create check function
    if nextElement.tag != "identifier":
        print("error compiling let, missing identifier")
        return -1
    #-------adding the first child to the let wrapper---------
    letWrapper.insert(childCounter,nextElement)
    counter += 1
    childCounter += 1
    
    nextElement = getNextElement(counter)
    
    if nextElement.text.strip() != "=":
        print("error compiling let, missing =")
        return -1
    letWrapper.insert(childCounter,nextElement)
    counter += 1
    childCounter += 1
    
    # counter = compileExpression(counter)
    counter += 1
    
    nextElement = getNextElement(counter)
    
    if nextElement.text.strip() != ";":
        print("error compiling let, missing ; at",counter)
        return -1
    letWrapper.insert(childCounter,nextElement)
    counter += 1
    
    root.insert(index,letWrapper)
    test = root[index+1]
    print(test.tag)
    root.remove(test)
    
    return counter
    
    
    
    
compileLet(33)
        
    
    
    
        
    


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
           
       
    
    
    
#---------------print the xml file
print(ET.tostring(root, encoding='utf8').decode('utf8'))