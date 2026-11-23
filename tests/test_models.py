import pytest

from classroom_catalog.models import Classroom
from classroom_catalog.errors import InvalidItemError

def test_valid_classroom():
    room = Classroom(
        item_id="301",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=3,
        capacity=25,
        occupied=False,
    )
    assert room.item_id == "301"
    assert room.name == "Компьютерный класс"
    assert room.category == "Лаборатория"
    assert room.year == 2020
    assert room.floor == 3
    assert room.capacity == 25
    assert room.occupied is False


def test_null_id():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="   ",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_invalid_id():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id= 123,
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_null_name():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="   ",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_invalid_name():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name=123,
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_null_category():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="    ",
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_invalid_category():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category=123,
            year=2020,
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_invalid_floor():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor="abc",
            capacity=10,
            occupied=False,
        )

def test_valid_big_floor():
    room = Classroom(
        item_id="301",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=7,
        capacity=25,
        occupied=False,
    )
    assert room.floor == 7

def test_valid_small_floor():
    room = Classroom(
        item_id="301",
        name="Компьютерный класс",
        category="Лаборатория",
        year=2020,
        floor=1,
        capacity=25,
        occupied=False,
    )
    assert room.floor == 1

def test_zero_floor():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=0,
            capacity=10,
            occupied=False,
        )

def test_small_floor():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=-1,
            capacity=10,
            occupied=False,
        )

def test_big_floor():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=103,
            capacity=10,
            occupied=False,
        )

def test_invalid_capacity():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity="abc",
            occupied=False,
        )

def test_small_capacity():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=-10,
            occupied=False,
        )

def test_invalid_occupied():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied="False",
        )

def test_num_occupied():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=2020,
            floor=3,
            capacity=10,
            occupied=12,
        )

def test_invalid_year():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year="2020",
            floor=3,
            capacity=10,
            occupied=False,
        )

def test_small_year():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=123,
            floor=3,
            capacity=10,
            occupied=False,
        )


def test_big_year():
    with pytest.raises(InvalidItemError):
        Classroom(
            item_id="301",
            name="Компьютерный класс",
            category="Лаборатория",
            year=1000000,
            floor=3,
            capacity=10,
            occupied=False,
        )