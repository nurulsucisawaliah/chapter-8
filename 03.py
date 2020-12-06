Mhs = []
while True:
    namaMhs = input('Nama : ')
    Mhs.append(namaMhs)
    ulangi = input('ulangi? ')
    if(ulangi != 'y'):
        break
        
print()
Mhs.sort()
for i in range(len(Mhs)):
    print (Mhs[i], '(', len(Mhs[i]), 'karakter)')

