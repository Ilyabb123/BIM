def find_common_participants(participants_1, participants_2, argument=','):

    participants_list_first = participants_1.split(argument)
    participants_list_second = participants_2.split(argument)

    total_participants = list(set(participants_list_first).intersection(participants_list_second))
    total_participants.sort()

    return total_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))


# TODO Провеьте работу функции с разделителем отличным от запятой
