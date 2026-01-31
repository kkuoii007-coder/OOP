class Store:
    def __init__(self, name, adress, items):
        self.name = name
        self.adress = adress
        self.items = items  # items — это словарь: { "товар": цена }


store1 = Store("Матрешка", "г. Москва, ул. Фестивальная, д. 14", {"вишня": 5, "бананы": 10})
store2 = Store("Алена", "г. Москва, ул. Смольная, д. 15", {"газировка": 12, "шоколад": 15})


def add_items(name, new_items):
    if name == store1.name:
        store = store1
    else:
        store = store2
    store.items.update(new_items)

def remove_item(name, key):
    if name == store1.name:
        store = store1
    else:
        store = store2
    removed_value = store.items.pop(key, None)

def up_items(name, new_items):
    if name == store1.name and adress == store1.adress:
        store = store1
    else:
        store = store2
    store.items.update(new_items)

def get_item(name, key):
    if name == store1.name:
        store = store1
    else:
        store = store2
    return store.items.get(key, None)



add_items("Матрешка",  {"творог": 6, "хлеб": 8})
print(store1.items)

ok = remove_item("Матрешка",  "бананы")
print(store1.items)

add_items("Матрешка", {"творог": 50})
print(store1.items)

price = get_item("Матрешка",  "вишня")
print(price)

price = get_item("Матрешка",  "бананы")
print(price)
