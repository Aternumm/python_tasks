number_of_floors = 9
number_of_flats_per_floor = 4

current_flat = int(input('Введите номера квартиры: '))


current_entrance = (current_flat - 1) // (number_of_floors * number_of_flats_per_floor) + 1

tmp = (current_entrance - 1) * (number_of_floors * number_of_flats_per_floor)
flat_in_entrance = current_flat - tmp
current_floor = (flat_in_entrance - 1) // number_of_flats_per_floor + 1

print(current_entrance, current_floor, sep='; ')
