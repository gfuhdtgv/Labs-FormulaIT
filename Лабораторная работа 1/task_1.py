numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None)
sum_numbers = sum(numbers[:missing_index]) + sum(numbers[missing_index + 1:])
len_numbers = len(numbers)
average_numbers = sum_numbers/len_numbers
numbers[4] = average_numbers
print("Измененный список:", numbers)
