from project_1.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    # create a class counter for all customers
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        # create an individual id for each customer
        self.id = self.get_next_id()
        # increment the counter for the next customer
        self.increment_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"