from dataclasses import asdict #преобразовывает автоматически в словарь
import json
from .catalog import Catalog
from .models import Classroom
from .errors import CorruptedFileError, UnsupportedVersionError, DublicateIDError, InvalidItemError

FORMAT_VERSION = 1 #константа версии файла


def save(catalog: Catalog, path: str) -> None:
    items = []
    for room in catalog:
        items.append(asdict(room))

    data = {"format_version": FORMAT_VERSION, "items": items }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load(catalog: Catalog, path: str) -> None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise CorruptedFileError("повреждённый JSON") from error
    if not isinstance(data, dict):
        raise CorruptedFileError("файл не является словарем")
    if "format_version" not in data or "items" not in data:
        raise CorruptedFileError("в файле нет одного из обязательных полей")
    if not isinstance(data["items"], list):
        raise CorruptedFileError("data[items] не является списком")
    if type(data["format_version"]) is not int:
        raise CorruptedFileError("версия не является целым числом")
    if data["format_version"] != FORMAT_VERSION:
        raise UnsupportedVersionError("версии не совпадают")

    temp_catalog = Catalog()
    for room_data in data["items"]:
        if not isinstance(room_data, dict):
            raise CorruptedFileError("room_data не является словарем")
        try:
            room = Classroom(**room_data) #распаковка словаря
            temp_catalog.add(room)
        except (TypeError, InvalidItemError, DublicateIDError) as error:
            raise CorruptedFileError("Некорректные данные аудитории") from error

    catalog._replace_from(temp_catalog)