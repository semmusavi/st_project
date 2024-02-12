import sqlite3
from recipe import Recipe

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            ingredients TEXT NOT NULL,
                            instructions TEXT NOT NULL
                        )''')
        self.conn.commit()

    def insert_recipe(self, recipe):
        cursor = self.conn.cursor()
        ingredients_str = ', '.join(recipe.ingredients)  # Serialize ingredients list to a string
        cursor.execute('''INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)''',
                       (recipe.title, ingredients_str, recipe.instructions))
        self.conn.commit()

    def search_recipe(self, title):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM recipes WHERE title LIKE ?''', ('%' + title + '%',))
        rows = cursor.fetchall()
        return [Recipe(*row[1:]) for row in rows]

    def delete_recipe(self, title):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM recipes WHERE title = ?''', (title,))
        self.conn.commit()

    def update_recipe(self, old_title, new_recipe):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE recipes SET title=?, ingredients=?, instructions=? WHERE title=?''',
                       (new_recipe.title, new_recipe.ingredients, new_recipe.instructions, old_title))
        self.conn.commit()

    def get_all_recipes(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM recipes''')
        rows = cursor.fetchall()
        return [Recipe(*row[1:]) for row in rows]

    def close(self):
        self.conn.close()
