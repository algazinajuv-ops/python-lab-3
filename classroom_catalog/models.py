from dataclasses import dataclass
from .errors import InvalidItemError

@dataclass
class Classroom():
    item_id: str
    name: str
    category: str
    year: int
    floor: int
    capacity: int
    occupied: bool

    def __post_init__(self): #проверка полей

        fields = {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
        }
        for field_name, value in fields.items():
            if not isinstance(value, str):
                raise InvalidItemError(f"{field_name} должен быть строкой")
            if not value.strip():
                raise InvalidItemError(f"{field_name} не может быть пустым")

        if type(self.floor) is not int:
            raise InvalidItemError("floor должен быть числом")
        if not (1<=self.floor<=7):
            raise InvalidItemError("floor должен быть:{1;7}")

        if type(self.year) is not int:
            raise InvalidItemError("year должен быть целым числом")
        if not (1900<=self.year<=2026):
            raise InvalidItemError("year должен быть:{1900;2026}")

        if type(self.capacity) is not int:
            raise InvalidItemError("capacity должен быть целым числом")
        if self.capacity<=0:
            raise InvalidItemError("capacity должен быть > 0")

        if type(self.occupied) is not bool:
            raise InvalidItemError("occupied должен быть булевой переменной")


                
