from collections.abc import Iterator
from .models import Classroom
from .errors import DublicateIDError, InvalidItemError, ItemNotFoundError
class Catalog:
    def __init__(self):
        self._items = {} #

    def add(self, item: Classroom)->None:
        if not isinstance(item, Classroom):
            raise InvalidItemError("неверный аргумент")
        if item.item_id in self._items:
            raise DublicateIDError("такой id уже есть")
        self._items[item.item_id] = item

    def get(self, item_id:str)->Classroom:
        if not isinstance(item_id, str):
            raise InvalidItemError("item_id должен быть строкой")
        if item_id in self._items:
            return self._items[item_id]
        raise ItemNotFoundError("такого item_id нет")

    def remove(self, item_id:str)->None:
        if not isinstance(item_id, str):
            raise InvalidItemError("item_id должен быть строкой")
        if item_id not in self._items:
            raise ItemNotFoundError("такого item_id нет")
        del self._items[item_id]

    def find_by_category(self, category: str)-> list[Classroom]:
        if not isinstance(category, str):
            raise InvalidItemError("category должен быть строкой")
        result = []
        for room in self._items.values():
            if room.category == category:
                result.append(room)

        return result

    def find_by_name(self, name:str)->list[Classroom]:
        if not isinstance(name, str):
            raise InvalidItemError("name должен быть строкой")
        result = []
        for room in self._items.values():
            if name.lower() in room.name.lower():
                result.append(room)
                
        return result

    def __len__(self)->int:
        return len(self._items)

    def __iter__(self)->Iterator[Classroom]:
        return iter(self._items.values())
        

    def __contains__(self, item_id:str)->bool:
        return item_id in self._items