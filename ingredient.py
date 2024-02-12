class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Ingredient(name={self.name}, quantity={self.quantity})"
