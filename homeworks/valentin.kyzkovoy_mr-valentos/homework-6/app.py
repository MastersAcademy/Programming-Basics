from Concert import Concert
from Home import Home
from Studio import Studio

info = open("filejson.json", "w")

concert1 = Concert('TD 2400', '4', '800', 'Play loud')
studio1 = Studio('TS 500', '3', '400', 'Play clear')
home1 = Home('sven 3s', '2', '50', 'Just play')

print(concert1)
print(studio1.pik_power())
print(home1.column_type)
print(studio1.clean_sound())

studio1.toxml()

info.write(concert1.tojson())
info.close()


