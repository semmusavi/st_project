import json
from ingredient import Ingredient
from cookInstruction import CookInstruction
from recipe import Recipe


class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'recipes': []}


    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump({'recipes': data}, file, default=self.serialize_recipe, indent=2)

    def serialize_recipe(self, obj):
        if isinstance(obj, Recipe):
            return {
                'title': obj.title,
                'ingredients': [{'name': i.name, 'quantity': i.quantity} for i in obj.ingredients],
                'cook_instruction': obj.instructions.instruction  # fix this line
            }
        elif isinstance(obj, Ingredient):
            return {'name': obj.name, 'quantity': obj.quantity}
        elif isinstance(obj, CookInstruction):
            return {'description': obj.instruction}  # fix this line
        raise TypeError("Object not serializable")
