from pprint import pprint

def introspection_info(obj):
    return {
        'type': type(obj),
        'attributes': [element for element in dir(obj) if not callable(getattr(obj, element, None))],
        'methods': [element for element in dir(obj) if callable(getattr(obj, element, None))],
        'module': getattr(obj, '__module__', None),
        'test': getattr(obj, 'int'),
    }


class Test:
    def __init__(self, int):
        self.int = int

    def task(self):
        print(f'Задание выполнено: {self.int} раз(а)!. Я готов умереть!')


my_test = Test(42)
my_test.task()

test_info = introspection_info(my_test)
pprint(test_info)
