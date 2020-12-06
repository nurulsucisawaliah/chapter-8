print('Menu :')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data')
print()

sayur = ['bayam', 'kangkung', 'wortel', 'selada']  
pilih = input('Pilihan saya adalah : ')
if  pilih == 'A' :
    print('Tambah data sayur' +':' + str(sayur))
    newSayur = input('Masukan tambahan sayur : ')
    sayur.append(newSayur)
    print(sayur)
        
elif pilih =='B':
    print('Hapus data sayur' + ':' + str(sayur))
    delete = input('Masukan data sayur yang ingin dihapus: ')
    sayur.remove(delete)
    print(sayur)
        
elif pilih =='C':
    print('Tampilkan data')
    print(sayur)
          
else:
    print()
        
       
