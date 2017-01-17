def obj_to_xml(objects, file_name):

    f = open(file_name, 'w')

    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    f.write("<object>\n")
    for obj in objects:
        json_dict = obj.__dict__
        f.write("\t<%s>\n" % obj.name.replace(" ", "_"))
        for key in json_dict:
            f.write("\t\t<%s>%s</%s>\n" % (key, str(json_dict[key]), key))
        f.write("\t</%s>\n" % obj.name.replace(" ", "_"))
    f.write("</object>\n")
    f.close()


def obj_to_json(objects, file_name):

    f = open(file_name, 'w')
    f.write("{\n\n")

    i = 0
    for obj in objects:
        json_dict = obj.__dict__
        f.write("\t\"%s\": {\n" % obj.name.replace(" ", "_"))
        j = 0
        for key in json_dict:
            if type(json_dict[key]) == str:
                f.write("\t\t\"%s\": \"%s\"" % (key, json_dict[key]))
            elif type(json_dict[key]) == int:
                f.write("\t\t\"%s\": %d" % (key, json_dict[key]))
            else:
                f.write("\t\t\"%s\": %s" % (key, str(json_dict[key]).replace("\'", "\"")))

            j += 1
            if j == len(json_dict):
                f.write("\n")
            else:
                f.write(",\n")
        i += 1
        if i == len(objects):
            f.write("\t}\n\n")
        else:
            f.write("\t},\n\n")

    f.write('}\n')

    f.close()

