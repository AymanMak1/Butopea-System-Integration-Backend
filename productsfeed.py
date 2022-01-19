import sqlite3
import pandas as pd
import xml.etree.ElementTree as xml

conn = sqlite3.connect("./data.sqlite")
cur = conn.cursor()
query1='SELECT p.product_id as ID,'\
        'pd.name as title,'\
        'pd.description,'\
        '"https://butopea.com/" || p.image as image_link,'\
        'p.price, m.name as brand '\
        'FROM product p,'\
        'product_description pd,'\
        'manufacturer m '\
        'WHERE p.product_id = pd.product_id AND '\
        'm.manufacturer_id = p.manufacturer_id '\
        'AND status = "1";'\
        

root = xml.Element("Products")

def GenerateXML(fileName):
    df = pd.read_sql(query1, conn)
    for i in range(len(df)) :
        child = xml.Element("Product")
        root.append(child)
        ID = xml.SubElement(child,"ID")
        ID.text = df.loc[i,"ID"]
        Title = xml.SubElement(child,"Title")
        Title.text = df.loc[i,"title"]
        Description = xml.SubElement(child,"Description")
        Description.text = df.loc[i,"description"]
        Link = xml.SubElement(child,"Link")
        Link.text = 'https://butopea.com/p/' + df.loc[i,"ID"]
        ImageLink = xml.SubElement(child,"ImageLink")
        ImageLink.text = df.loc[i,"image_link"]
        AdditionalImageLinks = xml.SubElement(child,"AdditionalImageLinks")
        query2 ='SELECT p.product_id as ID,'\
                 '"https://butopea.com/"|| pi.image AS additional_image_link,'\
                 'sort_order '\
                 'FROM product p, product_image pi '\
                 'WHERE pi.product_id = p.product_id AND '\
                 'p.product_id=' + str(df.loc[i,"ID"]) + ' AND status = "1" Order by sort_order;'\

        df2 = pd.read_sql(query2, conn)
        for j in range(len(df2)):
            AdditionalImageLinks.text = df2.loc[j,"additional_image_link"]
                
        Price = xml.SubElement(child,"Price")
        Price.text = df.loc[i,"price"]
        Brand = xml.SubElement(child,"Brand")
        Brand.text = df.loc[i,"brand"]
        Condition = xml.SubElement(child,"Condition")
        Condition.text = 'new'
        
    
    
    conn.close()
    tree = xml.ElementTree(root)
    with open(fileName,"wb") as feed:
        tree.write(feed)



if __name__ =="__main__":
    GenerateXML("feed.xml")
