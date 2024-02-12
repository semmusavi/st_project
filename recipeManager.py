from recipe import Recipe

class RecipeManager:
    def __init__(self, database):
        self.database = database

    def add_recipe(self, recipe):
        self.database.insert_recipe(recipe)

    def search_recipe(self, title_to_search):
        return self.database.search_recipe(title_to_search)

    def delete_recipe(self, title):
        self.database.delete_recipe(title)

    def update_recipe(self, old_title, new_recipe):
        self.database.update_recipe(old_title, new_recipe)

    def new_recipe_from_user(self):
        title = input("Enter the title of the recipe: ")
        ingredients = input("Enter ingredients (separated by commas): ").split(',')
        instructions = input("Enter cooking instructions: ")
        new_recipe = Recipe(title, ingredients, instructions)
        self.add_recipe(new_recipe)

    def get_all_recipes(self):
        return self.database.get_all_recipes()
