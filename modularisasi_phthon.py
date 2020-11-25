"""
program menghitung luas segitiga
= alas *tinggi /2
"""
print ('menghitung luas tanpa fungsi')
alas =12
tinggi = 4
luas_segitiga = alas *tinggi/2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi}memiliki luas{luas_segitiga}')

#definisikan fungsi

def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi /2
    return luas_segitiga
hitung_luas_segitiga(18,3)
hitung_luas_segitiga(10,3)
print(f'menghitung segitiga dengan fungsi.hasilnya= {hitung_luas_segitiga(18,3)}')
print(f'menghitung luas segitiga.hasilnya={hitung_luas_segitiga(10,5)}')