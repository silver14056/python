def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        return print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            if j != num_columns:
                print(operation(i, j), end=' ')
            else:
                print(operation(i, j))


print_operation_table(lambda x, y: x * y, 2, 2)
