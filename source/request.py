class Request:
    def __init__(self, request, storages, AbstractStorage):
        split_request = request.strip().lower().split(' ')
        if len(split_request) != 7:
            # Todo: Вывести ошибку, что запрос неправильный
            ...

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[3]
        self.destionation = split_request[6]

        if self.departure not in storages or self.destionation not in storages:
            # TODO: Вывести ошибку, что склад неизвестен
            ...