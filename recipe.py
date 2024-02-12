class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(title={self.title}, ingredients={self.ingredients}, instructions={self.instructions})"
