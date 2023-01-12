book_count = 10
print('Ibu berkata baca semua bukumu sampai paham')
read_count = 0

understood_count = 0
print(f'jumlah buku yang sudah dibaca :{understood_count}')

while read_count < book_count * 2:
        read_count = read_count + 1
        if understood_count == 9:
            print(f'Buku ke: {understood_count + 1} belum paham')
        else:
            understood_count = understood_count + 1
            print(f'Buku ke :{understood_count} sudah dibaca dan dipahami')

print(f'jumlah buku yang dibaca dan dipahami: {understood_count}')
if understood_count == book_count:
    print('Bu semua buku dah dipahami')

else:
    print(f'Bu, tidak semua buku bisa dipahami'
          f'Budi hanya bisa membaca {understood_count} buku')

