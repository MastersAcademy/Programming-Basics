class Gun(object):
    def __init__(self, company, model, issuance_year):
        self.company = company
        self.model = model
        self.issuance_year = issuance_year

    def output_gun(self):
        return print("Company '{0}', Model '{1}', issuance_year '{2}'".
                     format(self.company, self.model, self.issuance_year))

#gun1 = Gun("Тульський завод", "ТТ", "1930")
