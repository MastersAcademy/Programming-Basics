from OscillatingBait import OscillatingBait
from BaublesSpinner import BaublesSpinner
from SpoonBait import SpoonBait

oscillatingBait = OscillatingBait('red', '90%', '15g', '300kk')
baublesSpinner = BaublesSpinner('green', '80%', '10g', '200kk')
spoonBait = SpoonBait('white', '70%', '12g')


print(oscillatingBait)
print(baublesSpinner)
print(spoonBait.check_color())
