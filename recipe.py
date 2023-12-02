class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"{self.title}\nIngredients: {', '.join(map(str, self.ingredients))}\nInstructions: {self.instructions}"