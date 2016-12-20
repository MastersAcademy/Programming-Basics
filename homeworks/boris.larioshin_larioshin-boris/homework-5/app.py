from toothbrush import ToothBrush
from electrotoothbrush import ElectricToothBrush


br1 = ToothBrush('Colgate', 'medium', 'wood', 5, 2016, 11, 4)
br2 = ElectricToothBrush('OralB', 'medium', 'plastic', 6, 2016, 8, 25, 'Duracell')
print(br1)
br1.clean()
br1.applicability()
br1.about_brush()
print(br2)
br2.clean()
br2.applicability()
br2.about_electric_brush()
