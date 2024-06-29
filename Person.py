class Person:
    def __init__(self, first_name, last_name, country, state):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.state = state

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_location(self):
        return f"{self.country}, {self.state}"
