from dataclasses import dataclass

@dataclass
class Person:
    name: str
    sur_name: str
    street: str
    house_number: str
    zip_code: str
    phone_number: str

class AddressBook:
    def __init__(self) -> None:
        self._entries: list[Person] = []

    @property
    def entries(self):
        return self._entries
    
    def add_entry(self, person: Person):
        self._entries.append(person)


addr_book = AddressBook()
addr_book.add_entry(Person("Peter", "Hans", "LStr", "13a", "09579", "123"))
addr_book.add_entry(Person("Angela", "Merkel", "LStr", "13a", "09579", "123"))
print([x.street for x in addr_book.entries])
