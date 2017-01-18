from Armchair import Armchair


class Export (Armchair):
    def __init__(self, leg_num, material, cover, json_file, xml_file):
        Armchair.__init__(self, leg_num, material, cover)
        self.xml_file = xml_file
        self.json_file = json_file

    def sit(self):
        return "Its a comfortable %s armchair, have armrest ? %s, have backrest ? %s" % (self.cover,self.armrest, self.backrest)

    def export_json(self):
        json_data = open(self.json_file, "w")
        json_data.write("{\"Export\":{")
        json_data.write("\"leg_num\":\""+str(self.leg_num)+"\",")
        json_data.write("\"material\":\""+self.material+"\",")
        json_data.write("\"cover\":\""+self.cover+"\",")
        json_data.write("\"json_file\":\""+self.json_file+"\",")
        json_data.write("\"xml_file\":\""+self.xml_file+"\"}")
        json_data.write("}")
        json_data.close()

    def export_xml(self):
        xml_data = open(self.xml_file, "w")
        xml_data.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        xml_data.write("<Export>")
        xml_data.write("<leg_num>"+str(self.leg_num)+"</leg_num>")
        xml_data.write("<material>"+self.material+"</material>")
        xml_data.write("<cover>"+self.cover+"</cover>")
        xml_data.write("<json_file>"+self.json_file+"</json_file>")
        xml_data.write("<xml_file>"+self.xml_file+"</xml_file>")
        xml_data.write("</Export>")
        xml_data.close()

