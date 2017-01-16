class Gun(object):
    def __init__(self, company, model, fundation_year):
        self.company = company
        self.model = model
        self.fundation_year = fundation_year

    def output_gun(self):
        return print("Company '{0}', Model '{1}', fundation_year '{2}'".
                     format(self.company, self.model, self.fundation_year))

