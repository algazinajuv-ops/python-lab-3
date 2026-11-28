import pytest
import json
from dataclasses import asdict
from classroom_catalog.models import Classroom
from classroom_catalog.catalog import Catalog
from classroom_catalog.storage import save, load
from classroom_catalog.errors import (
    CorruptedFileError,
    UnsupportedVersionError
)

def test_round_trip(tmp_path):
    path = tmp_path / "catalog.json" #пайтест сам создаст веменную директорию
    catalog = Catalog()

    room1 = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    room2 = Classroom(
        "102", "Большая аудитория",
        "Лекционная", 2015, 2, 100, True
    )

    catalog.add(room1)
    catalog.add(room2)

    save(catalog, str(path))

    new_catalog = Catalog()

    load(new_catalog, str(path))

    assert list(new_catalog) == list(catalog)


def test_corrupted_json(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text('{"items": [', encoding="utf-8")

    catalog = Catalog()
    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))

def test_unsupported_version(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text(
        '{"format_version": 999, "items": []}',
        encoding="utf-8"
    )

    catalog = Catalog()

    with pytest.raises(UnsupportedVersionError):
        load(catalog, str(path))

def test_missing_field(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text(
        '{"format_version": 1}',
        encoding="utf-8"
    )

    catalog = Catalog()
    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))

def test_invalid_items_type(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text(
        '{"format_version": 1, "items": 123}',
        encoding="utf-8"
    )

    catalog = Catalog()

    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))

def test_invalid_room(tmp_path):
    path = tmp_path / "catalog.json"

    room = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    room_data = asdict(room)
    room_data["capacity"] = -10

    data = {
        "format_version": 1,
        "items": [room_data]
    }

    path.write_text(json.dumps(data), encoding="utf-8")

    catalog = Catalog()

    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))


def test_duplicate_id_in_file(tmp_path):
    path = tmp_path / "catalog.json"

    room = Classroom(
        "101", "Компьютерный класс",
        "Лаборатория", 2020, 1, 30, False
    )

    data = {
        "format_version": 1,
        "items": [asdict(room), asdict(room)]
    }

    path.write_text(json.dumps(data), encoding="utf-8")

    catalog = Catalog()

    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))


def test_atomic_load(tmp_path):
    path = tmp_path / "catalog.json"
    catalog = Catalog()

    original_room = Classroom(
        "101", "Старая аудитория",
        "Лекционная", 2020, 1, 30, False
    )

    catalog.add(original_room)

    valid_room = Classroom(
        "201", "Новая аудитория",
        "Лекционная", 2021, 2, 50, False
    )

    invalid_room = asdict(valid_room)
    invalid_room["item_id"] = "202"
    invalid_room["capacity"] = -10

    data = {
        "format_version": 1,
        "items": [asdict(valid_room), invalid_room]
    }

    path.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(CorruptedFileError):
        load(catalog, str(path))

    assert list(catalog) == [original_room]