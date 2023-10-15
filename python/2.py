pages = 100
lines = 50
sim = 25
one_sim = 4


byte_one_book = pages * lines * sim * one_sim
Mb_one_book = byte_one_book / (1024 * 1024)
books_all = int(1.44 // Mb_one_book, )

print("Количество книг, помещающихся на дискету:", books_all)
