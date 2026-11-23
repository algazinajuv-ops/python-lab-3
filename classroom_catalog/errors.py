class CatalogError(Exception):
    #Родительский класс
    pass

class InvalidItemError(CatalogError):
    #Сама аудитория содержит недопустимые данные
    pass

class DublicateIDError(CatalogError):
    #В каталоге уже есть аудитория с таким ID
    pass

class ItemNotFoundError(CatalogError):
    #Запрашиваемого ID нет в каталоге
    pass

class UnsupportedVersionError(CatalogError):
    #Версия JSON-формата не поддерживается
    pass

class CorruptedFileError(CatalogError):
    #JSON повреждён или имеет неправильную структуру
    pass
