users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique = set(users)
quantity_unique = len(unique)
quantity_users = len(users)
users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
total_number = {
    "Общее количество": quantity_users,
    "Уникальные посещения": quantity_unique
}
print(total_number)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
