print("============== menampilkan buah termahal ================")
print()
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

print('buah termahal adalah: ')
paling_mahal(buah)
print()

print("========== Menghitung rata-rata dari keseluruhan buah ==========")
print()
def ratanya(buah):
    ratanya = []
    for i in buah:
        rerata = list(buah.values())
        rata_rata = sum(rerata) / len(rerata)
        ratanya = [rata_rata]
    return ratanya

print('rata- rata harga satuan dari keseluruhan buah yang ada adalah : ')
print(ratanya(buah))
        
