# -*- coding: utf-8 -*-

import json

#  My base of players are in new_list_2.json
#  in such format [ {Key : value, Key_2 : value_2, Key_3 : value_3, ..........}
#                   {Key : value, Key_2 : value_2, Key_3 : value_3, ..........}
#                    {Key : value, Key_2 : value_2, Key_3 : value_3, ..........}
#                      .......
#                  ]


# open file and getting list
f = open('new_list_2.json', 'r')
json_string = f.readline()
parsed_string = json.loads(json_string)
f.close()

# print before changes
print(parsed_string[1])

# adding something to file
parsed_string[1]['Турнир_' + '21'] = 800

# saving to json file
# remove comments to work program correctly

f = open('new_list_2.json', 'w')
f.write(json.dumps(parsed_string))
f.close()

# open renewed file
f = open('new_list_2.json', 'r')
json_string = f.readline()
parsed_string = json.loads(json_string)
f.close()

# print after changes
print(parsed_string[1])

# converting to xml
f = open('new_list_2.xml', 'w')

i = 1
for el in parsed_string:
    f.write('<player_%s>' % i + '\n')
    i += 1
    for key, val in el.items():
        f.write('<%s>' % key + '\n')
        f.write('<value>' + '%s'%val + '</value>'+'\n')
        f.write('</%s>' % key + '\n')
    f.write('</player>' + '\n')
f.close()