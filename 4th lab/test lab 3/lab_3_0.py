def reverse_exercise(list_: list[int]) -> list[int]:
    # йдемо тільки до середини списку
    for i in range(len(list_) // 2):
        # міняємо перший і останній елемент місцями
        list_[i], list_[-i-1] = list_[-i-1], list_[i]

    return list_
