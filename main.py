from plistlib import Dict

from source.abstract_storage import AbstractStorage
from source.request import Request
from source.shop import Shop
from source.store import Store

store = Store(
    items={
        'картошка': 120,
        'яблоки': 86,
        'бананы': 74,
    },
    capacity=300)

shop = Shop(
    items={
        'картошка': 20,
        'яблоки': 18,
        'бананы': 10,
    },
    capacity=100,
    max_unique_items=5)

storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print('Добрый день!\n')

    while True:
        # TODO: Вывести содержимое складов
        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится:\n{storage.get_items()}')

        # TODO: Запросить у пользователя строку
        raw_request: str = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите  "stop" или "стоп", чтобы закончить')

        if raw_request in ('stop', 'стоп'):
            return

        # TODO: Обработать строку, проверить на ошибки, определить товар, количество, точки отправления и назначения
        request = Request(request=raw_request, storages=storages)

        # TODO: Доставить товар
        courier = Request(request=request, storages=storages)
        courier.move




if __name__ == '__main__':
    main()
