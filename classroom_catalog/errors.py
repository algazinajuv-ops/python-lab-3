class CatalogError(Exception):
    pass

class InvalidItemError(CatalogError):
    pass

class DublicateIDError(CatalogError):
    pass

class ItemNotFoundError(CatalogError):
    pass

class UnsupportedVersionError(CatalogError):
    pass

class CorruptedFileError(CatalogError):
    pass