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

def find_total_similarity_score_numbers(column1, column2):
    total = 0
    column1_copy = column1[:]
    column2_copy = column2[:]
    
    for i in range(len(column1_copy)):
        total += column1_copy[i] * column2_copy.count(column1_copy[i])

    print('Total :', total)


first_column, second_column = separate_columns()
find_total_similarity_score_numbers(first_column, second_column)