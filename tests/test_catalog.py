import pytest
from classroom_catalog.models import Classroom
from classroom_catalog.catalog import Catalog
from classroom_catalog.errors import (
    DublicateIDError,
    InvalidItemError,
    ItemNotFoundError
)


def test_add():
    catalog = Catalog()

    room = Classroom(
        item_id="101",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=1,
        capacity=30,
        occupied=False
    )

    catalog.add(room)

    assert len(catalog) ==1
    assert room.item_id in catalog
    assert catalog.get(room.item_id) == room

def test_add_dublicate():
    catalog = Catalog()

    room = Classroom(
        item_id="101",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=1,
        capacity=30,
        occupied=False
    )
    catalog.add(room)
    with pytest.raises(DublicateIDError):
        catalog.add(room)
    assert len(catalog) ==1

def test_add_invalid_item():
    catalog = Catalog()

    with pytest.raises(InvalidItemError):
        catalog.add('123')
    assert len(catalog)==0

def test_get():
    catalog = Catalog()

    room = Classroom(
        item_id="101",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=1,
        capacity=30,
        occupied=False
    )

    catalog.add(room)
    assert catalog.get("101") == room

def test_get_not_found():
    catalog = Catalog()
    with pytest.raises(ItemNotFoundError):
        catalog.get("999")


def test_get_invalid_id():
    catalog = Catalog()
    with pytest.raises(InvalidItemError):
        catalog.get(123)

def test_find_by_category():
    catalog = Catalog()

    room1 = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    room2 = Classroom(
        "102", "Большая аудитория",
        "Лекционная", 2015, 1, 100, False
    )

    room3 = Classroom(
        "103", "Класс информатики",
        "Лаборатория", 2022, 1, 25, False
    )

    catalog.add(room1)
    catalog.add(room2)
    catalog.add(room3)

    result = catalog.find_by_category("Лаборатория")

    assert len(result) ==2
    assert result == [room1, room3]

def test_find_by_name():
    catalog = Catalog()

    room1 = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    room2 = Classroom(
        "102", "Большая аудитория",
        "Лекционная", 2015, 1, 100, False
    )

    room3 = Classroom(
        "103", "Класс информатики",
        "Лаборатория", 2022, 1, 25, False
    )

    catalog.add(room1)
    catalog.add(room2)
    catalog.add(room3)

    result = catalog.find_by_name("КЛАСС")

    assert len(result) == 2
    assert result == [room1, room3]


def test_remove():
    catalog = Catalog()

    room = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    catalog.add(room)
    catalog.remove("101")
    assert len(catalog)==0
    assert "101" not in catalog


def test_remove_not_found():
    catalog = Catalog()

    with pytest.raises(ItemNotFoundError):
        catalog.remove("999")

def test_remove_invalid():
    catalog = Catalog()

    with pytest.raises(InvalidItemError):
        catalog.remove(123)

def test_len():
    catalog = Catalog()

    room = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    assert len(catalog)==0

    catalog.add(room)

    assert len(catalog)==1

    catalog.remove("101")

    assert len(catalog)==0




def test_contains():
    catalog = Catalog()

    room = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    catalog.add(room)
    assert "101" in catalog
    assert "999" not in catalog


def test_iter():
    catalog = Catalog()

    room1 = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    room2 = Classroom(
        "102", "Большая аудитория",
        "Лекционная", 2015, 1, 100, False
    )

    catalog.add(room1)
    catalog.add(room2)

    assert list(catalog) == [room1, room2]




def test_category_no_matches():
    catalog = Catalog()
    room1 = Classroom(
            "101", "Компьютерный класс",
            "Лаборатория", 2020, 1, 30, False
        )
    catalog.add(room1)
    assert catalog.find_by_category("999") == []

def test_name_no_matches():
    catalog = Catalog()
    room1 = Classroom(
            "101", "Компьютерный класс",
            "Лаборатория", 2020, 1, 30, False
        )
    catalog.add(room1)
    assert catalog.find_by_name("999") == []


def test_category_invalid_type():
    catalog = Catalog()
    room1 = Classroom(
            "101", "Компьютерный класс",
            "Лаборатория", 2020, 1, 30, False
        )
    catalog.add(room1)
    with pytest.raises(InvalidItemError):
        catalog.find_by_category(111)

def test_name_invalid_type():
    catalog = Catalog()
    room1 = Classroom(
            "101", "Компьютерный класс",
            "Лаборатория", 2020, 1, 30, False
        )
    catalog.add(room1)
    with pytest.raises(InvalidItemError):
        catalog.find_by_name(123)

def test_search_independence():
    catalog = Catalog()
    room1 = Classroom(
            "101", "Компьютерный класс",
            "Лаборатория", 2020, 1, 30, False
        )
    catalog.add(room1)
    result = catalog.find_by_category("Лаборатория")
    result.clear()
    assert catalog.find_by_category("Лаборатория") ==[ room1]
    assert len(catalog)==1
    assert "101" in catalog    
