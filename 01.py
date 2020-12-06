n_bbulat = int(input('berapa banyak bilangan bulat n buah? '))

m = 0
bilangan = []
while (m < n_bbulat):
    bil_bulat = int(input('Bilangan Bulat : '))
    bilangan = bilangan + [bil_bulat]
    m += 1
    
bilangan.sort()
bilangan.reverse()
print(bilangan)
