numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_none = numbers[0:4]
numbers_none2 = numbers[5:]
numbers_none3 = numbers_none + numbers_none2
summ_num = sum(numbers_none3)
quantity_num = len(numbers)
average_num = round(summ_num/quantity_num, 2)
numbers[4] = average_num

print("Измененный список:", numbers)

