# Завдання № 1

# Клас "тварина"
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound"

# Наслідування
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Приклад поліморфізму
def make_sound(animal):
    return animal.sound()

dog = Dog("Betty")
cat = Cat("Neko")

# Використання одного методу для різних об'єктів
print(make_sound(dog))  # Виведе: "Bark"
print(make_sound(cat))  # Виведе: "Meow"

animals = [
    Dog("Bob"),
    Cat("Galaxy devourer"),
    Dog("Rex")
]

# Поліморфне виконання методу sound() для кожної тварини
for animal in animals:
    print(f"{animal.name} says: {animal.sound()}")
    # Виведе:
    # Bob says: Bark
    # Galaxy devourer says: Meow
    # Rex says: Bark

# Завдання № 2

def merge_and_sort(list1, list2):
    # Об'єднуємо два списки
    combined_list = list1 + list2

    # Видаляємо повторення
    unique_list = list(set(combined_list))

    # Сортуємо
    unique_list.sort()

    return unique_list

# Тестові дані
list1 = ["apple", "banana", "cherry", "apple", "something"]
list2 = ["banana", "date", "elderberry", "something"]

# Тест функції
func_result = merge_and_sort(list1, list2)
print(func_result)  # Виведе: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'something']
