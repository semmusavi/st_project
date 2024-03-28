import unittest
import os
from unittest.mock import MagicMock
from recipeManager import RecipeManager
from recipe import Recipe
from ingredient import Ingredient
from cookInstruction import CookInstruction
from main import RecipeBook
from database import Database

class TestRecipeManager(unittest.TestCase):
    def setUp(self):
        self.database = MagicMock()
        self.recipe_manager = RecipeManager(self.database)

    def test_add_recipe(self):
        # Here the add recipe will be tested
        # Arrange 
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test Instructions")
        
        # Act
        self.recipe_manager.add_recipe(recipe)
        
        # Assert
        self.database.insert_recipe.assert_called_once_with(recipe)

class TestRecipeBook(unittest.TestCase):
    def setUp(self):
        self.database = MagicMock()
        self.recipe_manager = RecipeManager(self.database)
        self.recipe_book = RecipeBook()

    def test_run(self):
        # Arrange
        self.recipe_book.run = MagicMock()
        
        # Act
        self.recipe_book.run()
        
        # Assert
        self.recipe_book.run.assert_called_once()

class TestRecipe(unittest.TestCase):
    def test_repr(self):
        # Arrange
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test Instructions")
        
        # Act
        result = repr(recipe)
        
        # Assert
        self.assertEqual(result, "Recipe(title=Test Recipe, ingredients=['ingredient1', 'ingredient2'], instructions=Test Instructions)")

class TestIngredient(unittest.TestCase):
    def test_repr(self):
        # Arrange
        ingredient = Ingredient("Test Ingredient", "1 cup")
        
        # Act
        result = repr(ingredient)
        
        # Assert
        self.assertEqual(result, "Ingredient(name=Test Ingredient, quantity=1 cup)")


class TestCookInstruction(unittest.TestCase):
    def test_repr(self):
        # Arrange
        instruction = CookInstruction("Test Instruction")
        
        # Act
        result = repr(instruction)
        
        # Assert
        self.assertEqual(result, "CookInstruction(instruction=Test Instruction)")

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Create a test database
        self.db = Database('test.db')

    def tearDown(self):
        # Delete the test database after each test
        self.db.close()
        os.remove('test.db')

    def test_insert_recipe(self):
        # Arrange
        recipe = Recipe("Test Recipe", ["ingredient1", "ingredient2"], "Test Instructions")
        
        # Act
        self.db.insert_recipe(recipe)
        
        # Assert
        # Fetch the recipe from the database
        recipes = self.db.search_recipe("Test Recipe")
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].title, "Test Recipe")
        self.assertEqual(recipes[0].ingredients, ["ingredient1", "ingredient2"])
        self.assertEqual(recipes[0].instructions, "Test Instructions")

if __name__ == '__main__':
    unittest.main()
