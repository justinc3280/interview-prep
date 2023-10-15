class Inventory:
    def __init__(self):
        self._items = set()

    def add(self, name):
        if len(self._items) < 10:
            self._items.add(name)

    def remove(self, name):
        self._items.remove(name)

    def get_list(self):
        if len(self._items) > 0:
            print(','.join(self._items))
        else:
            print('No Items')

inventory = Inventory()

inventory.add('apple')
inventory.add('apple')
inventory.get_list()
