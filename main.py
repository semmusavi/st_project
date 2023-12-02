from recipeManager import RecipeManager
from database import Database

class RecipeBook:
    
    def __init__(self):
        self.database = Database("recipes.json")
        self.recipe_manager = RecipeManager(self.database)

    def print_menu(self):
        print("\n=== Recipe Book Menu ===")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Delete Recipe")
        print("4. Update Recipe")
        print("5. View All Recipes")
        print("6. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                print("add_recipe")
                self.recipe_manager.new_recipe_from_user()
                print("Recipe added successfully!")
            elif choice == '2':
                print("search_recipe")
                #search_recipe(self.recipe_manager)
            elif choice == '3':
                print("delete_recipe")
                #delete_recipe(self.recipe_manager)
            elif choice == '4':
                print("update_recipe")
                #update_recipe(self.recipe_manager)
            elif choice == '5':
                print("view_all_recipes")
                #view_all_recipes(self.recipe_manager)
            elif choice == '6':
                print("Exiting the Recipe Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    recipe_book = RecipeBook()
    recipe_book.run()
