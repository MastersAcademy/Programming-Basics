from Export import Export

newchair = Export(8,"metal","silk","file.json","file.xml")

newchair.export_json()
newchair.export_xml()
print (newchair.sit())

