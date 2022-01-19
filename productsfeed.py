import xml.etree.ElementTree as xml
root = xml.Element("Products")

def GenerateXML(fileName):
 
    child = xml.Element("Product")
    root.append(child)
    ID = xml.SubElement(child,"ID")
    Title = xml.SubElement(child,"Title")
    Description = xml.SubElement(child,"Description")
    Link = xml.SubElement(child,"Link")
    Image = xml.SubElement(child,"Image")
    ImageLink = xml.SubElement(child,"ImageLink ")
    AdditionalImageLinks = xml.SubElement(child,"AdditionalImageLinks")
    Price = xml.SubElement(child,"Price")
    Brand = xml.SubElement(child,"Brand")
    Condition = xml.SubElement(child,"Condition")
    ID.text = "196"

    tree = xml.ElementTree(root)
    with open(fileName,"wb") as feed:
        tree.write(feed)



if __name__ =="__main__":
    GenerateXML("feed.xml")
