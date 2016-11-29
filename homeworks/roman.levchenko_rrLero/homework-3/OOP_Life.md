**Sample Tennis Racquet**
-------------------------
**Class**
------------
_Class = Tennis Racquet_   
> I follow method Single responsibility Description of racquet 
> if i want add in my class Painting in some colour i will add another class painting racquet 

**Methods:**

* set GripSize,
* set Head size,
* set Weight,
* set Brand

**Objects:**

* Tennis racquet with GripSize = 4 3/8, Head size = 630 cm**2, Weight = 320 g, Brand = Babolat
* Tennis racquet with GripSize = 4 1/2, Head size = 690 cm**2, Weight = 290 g, Brand = Wilson

**Inheritance**
----------------
_Racquet for squash_

Class Racquet for squash = Class Tennis raquet + add another geometry of head

**Method:** 

* change geometry of head

**Object:** 

* Racquet for squash with triangle geometry with GripSize = 3, Head size = 450 cm**2, Weight = 250 g, Brand = Nike

**encapsulation**
-------------------
_Class = Tennis Racquet_   

**public:**

* GripSize,
* Head size,
* Weight,
* Brand

**protected:**

* string tension
* material of racquet
* micro cheap inside
* vibro damper

**abstract**
----------------
* level 1 = Tennis Raquet with HeadSize 630 cm**2 and Strings 
* level 2 = Racquet with strings
* Level 3 = Racquet to play some sport
* Level 4 = Some Object with unknown geometry

> Interface segregation: in my sample i have to divide my methods, because a lot of interfaces its bad.
> I have to separate Class on two Classes: Class Racquet Brand, and Class Racquet Characteristics 