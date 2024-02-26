from recipeManager import RecipeManager
from database import Database
from recipe import Recipe

class RecipeBookInterpreter:
    def __init__(self):
        self.database = Database("recipes.db")
        self.recipe_manager = RecipeManager(self.database)

    def interpret_dsl_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.execute_action(line)

    def execute_action(self, action_line):
        if ":" in action_line:
            action, data = action_line.split(":", 1)
            action = action.strip()
            args = eval(data.strip())
        else:
            action = action_line.strip()
            args = []

        if action == "Add Recipe":
            title, ingredients, instructions = args
            new_recipe = Recipe(title, ingredients, instructions)
            self.recipe_manager.add_recipe(new_recipe)
            print("Recipe added successfully!")
        elif action == "Search Recipe":
            title = args[0]
            found_recipes = self.recipe_manager.search_recipe(title)
            if found_recipes:
                for recipe in found_recipes:
                    print(recipe)
            else:
                print("No recipes found.")
        elif action == "Delete Recipe":
            title = args[0]
            self.recipe_manager.delete_recipe(title)
            print("Recipe deleted successfully!")
        elif action == "Update Recipe":
            old_title, new_title, ingredients, instructions = args
            updated_recipe = Recipe(new_title, ingredients, instructions)
            self.recipe_manager.update_recipe(old_title, updated_recipe)
            print("Recipe updated successfully!")
        elif action == "View All Recipes":
            all_recipes = self.recipe_manager.get_all_recipes()
            for recipe in all_recipes:
                print(recipe)
        else:
            print("Invalid action.")


if __name__ == "__main__":
    interpreter = RecipeBookInterpreter()
    interpreter.interpret_dsl_file("d:/st_project/recipe_book_data.dsl")
