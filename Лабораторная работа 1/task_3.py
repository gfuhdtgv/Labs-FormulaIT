# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 #мегабайты
page = 100
str_ = 50
symbol = 25
volume_symbol = 4 #байты

len_symbol = page * symbol * str_ #кол-во символов в книге
byte_1_book = len_symbol * volume_symbol #всего байт в 1 книге
volume *= 1024 * 1024 #перевод Мб в байты
result = int(volume//byte_1_book)

print("Количество книг, помещающихся на дискету:", result)
