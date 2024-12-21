import unittest

from exam import *

class TestAnimalClasses(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо об'єкти перед тестами
        self.dog = Dog("Betty")
        self.cat = Cat("Neko")
        self.animal = Animal("Generic")

    def test_animal_initialization(self):
        # Перевіримо ініціалізацію класу Animal
        self.assertEqual(self.animal.name, "Generic")
        self.assertEqual(self.animal.sound(), "Some generic sound")

    def test_dog_initialization_and_inheritance(self):
        # Перевіримо ініціалізацію класу Dog
        self.assertEqual(self.dog.name, "Betty")
        self.assertIsInstance(self.dog, Animal)
        self.assertEqual(self.dog.sound(), "Bark")

    def test_cat_initialization_and_inheritance(self):
        # Перевіримо ініціалізацію класу Cat
        self.assertEqual(self.cat.name, "Neko")
        self.assertIsInstance(self.cat, Animal)
        self.assertEqual(self.cat.sound(), "Meow")

    def test_make_sound_function(self):
        # Перевіримо нашу поліморфну поведінку и функцію make_sound
        self.assertEqual(make_sound(self.dog), "Bark")
        self.assertEqual(make_sound(self.cat), "Meow")
        self.assertEqual(make_sound(self.animal), "Some generic sound")

class TestListMerging(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо наші списки перед тестами
        self.list1 = ["apple", "banana", "cherry"]
        self.list2 = ["banana", "date", "elderberry"]

    def test_merge_and_sort_basic(self):
        # Перевіримо що функція реально сортує і працює
        expected = ["apple", "banana", "cherry", "date", "elderberry"]
        result = merge_and_sort(self.list1, self.list2)
        self.assertEqual(result, expected)

    def test_merge_and_sort_with_duplicates(self):
        # Перевіримо що буде якщо дати багато повторювань
        list1 = ["apple", "apple", "banana"]
        list2 = ["banana", "banana", "cherry"]
        expected = ["apple", "banana", "cherry"]
        result = merge_and_sort(list1, list2)
        self.assertEqual(result, expected)

    def test_merge_and_sort_empty_lists(self):
        # Перевіримо поведінку з порожнім списком
        self.assertEqual(merge_and_sort([], []), [])
        self.assertEqual(merge_and_sort(["apple"], []), ["apple"])
        self.assertEqual(merge_and_sort([], ["banana"]), ["banana"])

    def test_merge_and_sort_case_sensitivity(self):
        # Перевіримо чи впливає регістр (верхній, чи нижній)
        list1 = ["Apple", "banana"]
        list2 = ["Cherry", "date"]
        expected = ["Apple", "Cherry", "banana", "date"]
        result = merge_and_sort(list1, list2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()