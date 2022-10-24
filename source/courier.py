class Courier:
    def __int__(self, request, storages, AbstractStorage):
        self.__request = request

        self.departure: AbstractStorage = storages[self.__request.departure]
        self.destination: AbstractStorage = storages[self.__request.destination]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        print(f'Курьер везёт {self.__request.amount} {self.__request.product} '
              f'со {self.__request.departure}')

        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')