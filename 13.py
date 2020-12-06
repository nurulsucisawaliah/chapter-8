def max_nilai(nilaiMhs):
    mid = []
    uas = []
    hasilnya = []
    paling_tinggi = []
    for i in nilaiMhs:
        nilai_proses = i['mid'] + (2*i['uas'])
        nilai_akhir  = nilai_proses / 3
        hasilnya.append(nilai_akhir)
    paling_tinggi = hasilnya.index(max(hasilnya))
    terTinggi = {'nim': nilaiMhs[paling_tinggi]['nim'], 'nama' : nilaiMhs[paling_tinggi]['nama']}
    return terTinggi

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

tTinggi = max_nilai(nilaiMhs)
print('Mahasiswa yang memiliki nilai akhir tertinggi adalah : ' + str(tTinggi['nama']) + ',' + 'NIM' , tTinggi['nim'])
