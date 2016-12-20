from Fiction import Fiction
from Nonfiction import Nonfiction

book1 = Fiction("George Orwell", "1984", 1948, 267, "novel", "dystopian")
book2 = Nonfiction("Suetonius", "The Lives of the Caesars", 121, 363, "historical biography")

print(book1)
print(book2)

print(book1.info())
print(book1.current_reading())
print(book1.rating(1890))
      
      
print(book2.info())
print(book2.future_reading())
print(book2.availability(25))
      
      

