from django.test import TestCase

# Create your tests here.
{
   'id': 1, 'name': 'strogonoff 0', 'age': 2, 'weight': 10.2, 'sex': 'female', 'group': {'id': 1, 'scientific_name': 'canis familiaris', 'created_at': '2022-11-27T17:55:22.819371Z'}, 'traits': [{'id': 1, 'pets': [<Pet: Pet object (1)>, <Pet: Pet object (2)>, <Pet: Pet object (3)>, <Pet: Pet object (4)>, <Pet: Pet object (5)>], 'created_at': '2022-11-27T17:55:22.819371Z', 'trait_name': 'clever'}, {'id': 2, 'pets': [<Pet: Pet object (1)>, <Pet: Pet object (2)>, <Pet: Pet object (3)>, <Pet: Pet object (4)>, <Pet: Pet object (5)>], 'created_at': '2022-11-27T17:55:22.819371Z', 'trait_name': 'friendly'}]} not found in [{'id': 1, 'name': 'strogonoff 0', 'age': 2, 'weight': 10.2, 'sex': 'female', 'group': {'id': 1, 'scientific_name': 'canis familiaris', 'created_at': '2022-11-27T17:55:22.819371Z'}, 'traits': [{'id': 1, 'trait_name': 'clever', 'created_at': '2022-11-27T17:55:22.819371Z'}, {'id': 2, 'trait_name': 'friendly', 'created_at': '2022-11-27T17:55:22.819371Z'}]}, {'id': 2, 'name': 'strogonoff 1', 'age': 2, 'weight': 10.2, 'sex': 'female', 'group': {'id': 1, 'scientific_name': 'canis familiaris', 'created_at': '2022-11-27T17:55:22.819371Z'}, 'traits': [{'id': 1, 'trait_name': 'clever', 'created_at': '2022-11-27T17:55:22.819371Z'}, {'id': 2, 'trait_name': 'friendly', 'created_at': '2022-11-27T17:55:22.819371Z'}]}] : Verifique se sua rota está retornando todos os campos corretamente.
