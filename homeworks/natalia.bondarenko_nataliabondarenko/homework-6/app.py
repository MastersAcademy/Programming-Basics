from wheel import Wheel
from transport_wheels import TransportWheels
from files_handler import FilesHandler


prototype = TransportWheels()
print(prototype)
print(prototype.set_up())
# Implementation of homework-6 in the app:
print(prototype.key_value)
files_handler = FilesHandler()
files_handler.create_json_file(prototype.key_value)
files_handler.read_json_file('results.json')
files_handler.create_xml_file(prototype.key_value)
files_handler.read_xml_file('results.xml')

