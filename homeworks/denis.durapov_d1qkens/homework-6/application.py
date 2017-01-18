from SunGlasses import SunGlasses


print("We have trouble at hands. Let's find person who can solve it")

sunglasses = SunGlasses('RayBan_Aviator', 'carbon_fibre',
                        'polarized_green', 'pilot', "65", 'black')

# Converting object to JSON and saving in file
json_file = sunglasses.convert_to_json()
sunglasses.save_to_file(json_file)

# Converting object to XML and saving in file
xml_file = sunglasses.convert_to_xml()
sunglasses.save_to_file(xml_file)

