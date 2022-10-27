class BaseError(Exception):
    message = 'Что-то пошло не так'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class TooManyDifferentProductsError(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequestError(BaseError):
    message = 'Запрос неправильный'


class UnknownStorage(BaseError):
    message = 'Склад неизвестен'
