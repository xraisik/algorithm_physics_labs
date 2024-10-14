def reverse_exercise(list_: list[int]) -> list[int]:
    # йдемо тільки до середини списку
    for i in range(len(list_) // 2):
        # міняємо перший і останній елемент місцями
        list_[i], list_[-i-1] = list_[-i-1], list_[i]

    return list_

list_ = [1, 5, 10, 2]
print("Початковий список:", list_)

print("Зміненний список:",reverse_exercise(list_))

# перевіряємо ассертом
assert list_ == [2, 10, 5, 1]
print("Тест пройдено успішно!")