from Wired_phone import Wired_phone

class Radiophone_administration (Wired_phone):
    def __init__(self, color, model, inventory_number, appointment, convert_conversation_into_text_document, convert_conversation_into_audio):
        Wired_phone.__init__(self, color, model, inventory_number, appointment)
        self.convert_conversation_into_text_document = convert_conversation_into_text_document if convert_conversation_into_text_document else 'true'
        self.convert_conversation_into_audio = convert_conversation_into_audio if convert_conversation_into_audio else 'true'

    def convert_conversation_into_text_document(self, document):
        return 'The document \'%s\' was created' % document

    def convert_conversation_in_audio(self, mp3_document):
        return 'The document \'%s\' was created' % mp3_document

phone_head = Radiophone_administration('dark', 'AA2', 45, 'Use by chief', 'Can convert telephone conversations into text documents', 'Can convert telephone conversations into audio')
print('RADIOPHONE_ADMINISTRATION')
print(phone_head.appointment)
print(phone_head.convert_conversation_into_text_document)
print(phone_head.convert_conversation_into_audio)
