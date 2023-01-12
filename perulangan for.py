'''
perulangan for
'''

jumlah_buku = 10
print(" program baca semua buku")
jumlah_buku_yang_dibaca = 0
print(f'jumlah buku yang udah dibaca {jumlah_buku_yang_dibaca}')
"""
10 itu jumlah perulangannya, artinya index dari 0-9, 
"""
for jumlah_buku_yang_dibaca in range (1,11):
    print(f"Buku ke {jumlah_buku_yang_dibaca} yang sudah dibaca")
    print(f'jumlah buku yang udah dibaca {jumlah_buku_yang_dibaca}')

"""
atau cara lain
"""
for jumlah_buku_yang_dibaca in range (1,jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_dibaca} yang sudah dibaca")
