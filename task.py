# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(people_one,people_two, delimiter = ","):
    people1 = people_one.split(delimiter)
    people2 = people_two.split(delimiter)

    people3 = list(set(people1).intersection(people2))
    participiants_list = sorted(people3)

    return participiants_list
# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group))