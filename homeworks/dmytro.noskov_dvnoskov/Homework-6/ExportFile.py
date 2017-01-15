import json


print('Welcome to get started you need to select modes')
A = input(str('Select the type export  format JSON(1) or XML(2)'))
B = input(str('Enter the input name File'))
C = input(str('Enter the output name File'))
if A == '1':
    fin = open(B, 'rt')
    lines = fin.readlines()
    fin.close()
    Outfile = C + ".json"
    json.dump(lines, open(Outfile, 'w'))
else:
    fin = open(B, 'rt')
    lines = fin.readlines()
    fin.close()
    i = 0
    a = '<?xml version="1.0" encoding="UTF-8" ?>'
    Outfile2 = C + ".xml"
    out = open(Outfile2, 'w', encoding="utf-8")
    print(a, file=out)
    for line in lines:
        line2 = line.split('\n')
        line3 = " ".join(line2)
        i += 1
        line1 = '<' + str(i) + '>' + line3 + '</' + str(i) + '>'
        print(line1, file=out)
    out.close()

