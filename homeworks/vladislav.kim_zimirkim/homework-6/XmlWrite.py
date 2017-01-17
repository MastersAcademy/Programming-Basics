import xml.etree.cElementTree as Tree
from Gun import Gun
tar21 = Gun('TAR-21',5.56,460,'Auto',11)
tar21 = Tree.Element("Gun")
specification = Tree.SubElement(tar21, "specification")

Tree.SubElement(specification, "Name").text = "TAR-21"
Tree.SubElement(specification, "Caliber").text = "5.56"
Tree.SubElement (specification, "Barrel_length"). text = "460"
Tree.SubElement (specification, "Type_of_reload"). text = "Auto"
Tree.SubElement(specification, "Amount_of_ammo").text = "11"

wrt = Tree.ElementTree(tar21)
wrt.write(open("Gun.xml", 'wb'))