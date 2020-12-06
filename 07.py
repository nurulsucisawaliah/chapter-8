def paling_mahal(buah):
    list_buah = list(buah.keys())
    list_fruit = tuple(buah.values())
    harga_max = max(list_fruit)
    value_max = list_fruit.index(harga_max)
    print(list_buah[value_max])

buah = {'Apel'  : 5000,
        'Jeruk' : 8500,
        'Mangga': 7800,
        'Duku'  : 6500}

paling_mahal(buah)
