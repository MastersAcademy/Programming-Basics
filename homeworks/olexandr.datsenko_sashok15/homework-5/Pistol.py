from Gun import Gun


class PistolTT(Gun):
    def __init__(self, company, model, issuance_year):
        super().__init__(company, model, issuance_year)
        self.store = 8

    def fire(self):
        return print("Shop charged %s bullets. It shoots single rounds and discharged for 15 seconds."
                     % str(self.store))
