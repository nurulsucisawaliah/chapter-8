def kuadrat(bil):
    bilangan = []
    for i in range(len(bil)):
        pangkat2_kali = bil[i] * bil[i]
        bilangan.append(pangkat2_kali)
    return bilangan

listnya = [2,4,5,6]
hasil = kuadrat(listnya)
print('bil' + str(listnya))
print('hasil = kuadrat(bil)')
print('sehingga isi dari hasil berupa list dalam bentuk' + str(hasil))
print('sehingga isi dari hasil berupa list dalam bentuk' + str(hasil)
