from recipeManager import RecipeManager
from database import Database
# this is main file
class RecipeBook:
    """A simple recipe book application."""
    def __init__(self):
        """Initialize the RecipeBook."""
        self.database = Database("recipes.db")  
        self.recipe_manager = RecipeManager(self.database)

    def print_menu(self):
        """Display the menu options."""
        print("\n=== Recipe Book Menu ===")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Delete Recipe")
        print("4. Update Recipe")
        print("5. View All Recipes")
        print("6. Exit")

    def run(self):
        """Run the recipe book application."""
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                """Add a new recipe."""
                print("Add Recipe")
                self.recipe_manager.new_recipe_from_user()
                print("Recipe added successfully!")
            elif choice == '2':
                """Search for a recipe."""
                print("Search Recipe")
                title_to_search = input("Enter the title to search: ")
                found_recipes = self.recipe_manager.search_recipe(title_to_search)
                if found_recipes:
                    for recipe in found_recipes:
                        print(recipe)
                else:
                    print("No recipes found.")
            elif choice == '3':
                """Delete a recipe."""
                print("Delete Recipe")
                title_to_delete = input("Enter the title of the recipe to delete: ")
                self.recipe_manager.delete_recipe(title_to_delete)
                print("Recipe deleted successfully!")
            elif choice == '4':
                """Update a recipe."""
                print("Update Recipe")
                old_title = input("Enter the title of the recipe to update: ")
                new_recipe = self.recipe_manager.new_recipe_from_user()
                self.recipe_manager.update_recipe(old_title, new_recipe)
                print("Recipe updated successfully!")
            elif choice == '5':
                """View all recipes."""
                print("View All Recipes")
                all_recipes = self.recipe_manager.get_all_recipes()
                for recipe in all_recipes:
                    print(recipe)
            elif choice == '6':
                print("Exiting the Recipe Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    recipe_book = RecipeBook()
    recipe_book.run()
