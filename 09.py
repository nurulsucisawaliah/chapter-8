buah = {'Apel'  : 5000,
        'Jeruk' : 8500,
        'Mangga': 7800,
        'Duku'  : 6500}

fruit_name = list(buah)
fruit_harga = list(buah.values())

print("input-lah nama buah yang ingin dibeli dan berapa kg buah yang ingin dibeli")
beli_buah = input('Nama buah yang  dibeli : ')
kilo_gram = int(input('Berapa kg              : '))
print('------------------------------------')
harga_index = fruit_name.index(beli_buah)
fruit_beli = fruit_harga[harga_index] * kilo_gram 
print('total harga            :' + str(kilo_gram) +' /'  + 'kg')




