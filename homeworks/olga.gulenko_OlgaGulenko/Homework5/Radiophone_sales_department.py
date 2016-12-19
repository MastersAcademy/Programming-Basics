from Wired_phone import Wired_phone

class Radiophone_sales_department(Wired_phone):
    def __init__(self, color, model, inventory_number, appointment, anonymously_call):
        Wired_phone.__init__(self, color, model, inventory_number, appointment)
        self.anonymously_call = anonymously_call if anonymously_call else 'true'

    def anonymously_call (self):
        return 'Can call anonymously only'

    def convert_conversation_into_text_document(self):
        print('You have no access rights to convert conversation.')

phone_sales = Radiophone_sales_department('Color: brown', 'Model:You have no access rights to this information', 'Inventory number: you have no access rights to this information', 'Appointment: you have no access rights to this information', 'Can call only' )
print('PHONE SALES')
print(phone_sales.color)
print(phone_sales. model)
print(phone_sales.inventory_number)
print(phone_sales.appointment)
print(phone_sales.anonymously_call)
print(phone_sales.convert_conversation_into_text_document())





