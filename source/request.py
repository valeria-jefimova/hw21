from typing import Dict

from exceptions import InvalidRequestError, UnknownStorage
from source.abstract_storage import AbstractStorage


class Request:
    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        split_request: list[str] = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequestError

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[3]
        self.destionation = split_request[6]

        if self.departure not in storages or self.destionation not in storages:
            raise UnknownStorage
