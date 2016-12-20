from Pen import Pen


class Drawing_Pen(Pen):
    def __init__(self, name, barcode, size, material, line_thickness):
        super().__init__(name, barcode, size, material)
        self.line_thickness = line_thickness

    def council(self):
        print("It will be comfortable to use it for drawing thin lines.")

    def what_is_inside(self):
        print("It is not interesting, you can get dirty with ink!")