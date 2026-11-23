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