def separate_columns():
    first_column = []
    second_column = []

    with open("./data/day1_data.txt", "r") as f:
        lines = f.readlines()
        for line in lines[0:]:
            columns = line.strip().split()
            if len(columns) >= 2:
                first_column.append(float(columns[0]))
                second_column.append(float(columns[1]))
    return first_column, second_column

                
def find_total_deviation_numbers(column1, column2):
    total = 0
    column1_copy = column1[:]
    column2_copy = column2[:]
    
    while column1_copy and column2_copy: 
        deviation = abs(min(column1_copy) - min(column2_copy))
        total += deviation
        print(deviation)
        column1_copy.remove(min(column1_copy))
        column2_copy.remove(min(column2_copy))

    print("Total deviation:", total)


first_column, second_column = separate_columns()
find_total_deviation_numbers(first_column, second_column)
