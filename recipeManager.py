from ingredient import Ingredient
from cookInstruction import CookInstruction
from recipe import Recipe

class RecipeManager:
    def __init__(self, database):
        self.database = database
        self.recipes = self.database.load_data()

    # ... (other methods)

    def add_recipe(self, recipe):
        self.recipes['recipes'].append(recipe)
        self.database.save_data(self.recipes['recipes'])

    def search_recipe(self, title_to_search):
        return [recipe for recipe in self.recipes if title_to_search.lower() in recipe.title.lower()]

    def delete_recipe(self, title):
        self.recipes = [recipe for recipe in self.recipes if title.lower() != recipe.title.lower()]
        self.database.save_data(self.recipes)

    def update_recipe(self, old_title, new_recipe):
        # Find the index of the old recipe
        index_to_update = next((index for index, recipe in enumerate(self.recipes['recipes']) if recipe['title'].lower() == old_title.lower()), None)

        if index_to_update is not None:
            # Update the recipe at the found index
            self.recipes['recipes'][index_to_update] = new_recipe
            self.database.save_data(self.recipes['recipes'])
            print("Recipe updated successfully!")
        else:
            print("Recipe not found.")

    def new_recipe_from_user(self):
            title = input("Enter the title of the recipe: ")
            
            # Collect ingredients
            ingredients = []
            while True:
                ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
                if ingredient_name.lower() == 'done':
                    break
                quantity = input("Enter quantity: ")
                ingredients.append(Ingredient(ingredient_name, quantity))

            # Collect cook description
            instructions = input("Enter cook instructions: ")
            cook_instruction = CookInstruction(instructions)

            # Create a new recipe
            new_recipe = Recipe(title, ingredients, cook_instruction)

            # Add the new recipe to the recipes list
            self.add_recipe(new_recipe)
    
    def get_all_recipes(self):
        return [recipe['title'] for recipe in self.recipes['recipes']]
