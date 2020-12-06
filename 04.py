print('Menu :')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data')
print()

sayur = ('bayam', 'kangkung', 'wortel', 'selada')
pilih = input('Pilihan saya adalah : ')
if  pilih == 'A' :
    print('Tambah data sayur')
    print(sayur)
    vegetable = list(sayur)
    print()
    newSayur = input('Masukan tambahan sayur : ')
    vegetable.append(newSayur)
    sayur_mayur = tuple(vegetable)
    print(sayur_mayur)
        
elif pilih =='B':
    print('Hapus data sayur')
    print(sayur)
    vegetable = list(sayur)
    print()
    delete = input('Masukan data sayur yang ingin dihapus: ')
    vegetable.remove(delete)
    del_sayur = tuple(vegetable)
    print(del_sayur)
        
elif pilih =='C':
    print('Tampilkan data')
    print(sayur)
          
else:
    print()
        
       
