from source.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        if self.__get_free_space() < amount:
            # TODO: Вывести ошибку, что на складе недостаточно места
            ...

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] += amount

    def remove(self, name, amount):
        if name not in self.__items or self.__items[name] < amount:
            # TODO: Вывести ошибку, что на складе недостаточно товара
            ...

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
