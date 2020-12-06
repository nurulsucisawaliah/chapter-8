buah = {'Apel'  : 5000,
        'Jeruk' : 8500,
        'Mangga': 7800,
        'Duku'  : 6500}
print(buah)
fruit_name = list(buah)
fruit_harga = list(buah.values())
jumlah = []

while True:
    beli_buah = input('Nama buah yang  dibeli : ')
    kilo_gram = int(input('Berapa kg              : '))
    harga_index = fruit_name.index(beli_buah)
    fruit_beli = fruit_harga[harga_index] * kilo_gram
    jumlah.append(fruit_beli)
    print()
    buah_lain = input('Beli buah yang lain (y/n) ? ') 
    if buah_lain != 'y':
        break
    else:
        print()
total_beli = sum(jumlah)
print('------------------------------------------')
print('Total harga          :' + str(total_beli))
    
