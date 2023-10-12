from phonebook import PhoneBook


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Kasia", "123456789")
    phonebook.add("Michal", "000123")
    assert "123456789" == phonebook.lookup("Kasia")
    assert "000123" == phonebook.lookup("Michal")


def test_add_twice_then_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Kasia", "123456789")
    phonebook.add("Kasia", "000123")
    assert "000123" == phonebook.lookup("Kasia")