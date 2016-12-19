# Flying????

aircraft = input("We fly on a plane or a helicopter? Type plane or helicopter ")
trapdoor = input("Trapdoor open or close? ")
fuel= input ("Type fuel level - full or low ")

    if aircraft == 'plane':
        weight= int (input ("Type weight your plane "))
        from airplane import airplane
        plane = airplane (trapdoor,fuel,weight)
        print (plane.takeoff())
    elif aircraft=='helicopter':
        windspeed = int(input("Type windspeed "))
        from helicopter import helicopter
        helicopter = helicopter(trapdoor, fuel, windspeed)
        print(helicopter.takeoff())
    else:
        print ('Is no aircraft!')



