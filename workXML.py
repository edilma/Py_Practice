#Parsing and processing xml

import xml.dom.minidom
def main():
    #load and parse an xml file
    doc = xml.dom.minidom.parse("sampleXml.xml")
    
    #print out the document node and thename of the first child tag
    print (doc.nodeName)
    print( doc.firstChild.tagName)
    
    #get a list of XML tags from the document and print each
    skills = doc.getElementsByTagName ("skill")
    print(skills.length, "Skills are listed")
    for skill in skills:
        print (skill.getAttribute("name"))

    #Create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "AI")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName ("skill")
    
    print(skills.length, "Skills are listed")
    for skill in skills:
        print (skill.getAttribute("name"))



if __name__ == "__main__":
    main()