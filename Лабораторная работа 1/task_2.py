list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

k_list_players = int(len(list_players)/2) #половина кол-ва игроков в списке

# TODO Разделите участников на две команды
list_players_1 = list_players[:k_list_players]
list_players_2 = list_players[k_list_players:]

print(list_players_1) #Первая команда
print(list_players_2) #Вторая команда