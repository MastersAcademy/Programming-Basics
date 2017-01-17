try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from Fiction import Fiction
book1 = Fiction("George Orwell", "1984", 1948, 267, "novel", "dystopian")

book1 = ET.Element("book1")
data = ET.SubElement(book1, "data")

ET.SubElement(data, "author", data="author").text = "George Orwell"
ET.SubElement(data, "title", data="title").text = "1984"
ET.SubElement(data, "year_of_writing", data="year_of_writing").text = "1948"
ET.SubElement(data, "number_of_pages", data="number_of_pages").text = "267"
ET.SubElement(data, "form", data="form").text = "novel"
ET.SubElement(data, "kind", data="kind").text = "dystopian"

tree = ET.ElementTree(book1)
tree.write("fiction.xml")




