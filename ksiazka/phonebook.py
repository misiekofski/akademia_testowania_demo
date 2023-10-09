class PhoneBook():
    def __init__(self):
        self.numbers = {}

    def add(self, name, phone):
        self.numbers[name] = phone

    def lookup(self, name):
        return self.numbers[name]
