def get_data():
    datas = []

    with open("./data/day2_data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            datas.append(line.strip())
    return datas

def find_total_safe_lines():
    datas = get_data()
    total_safe_lines = 0

    for i in range(len(datas)):
        data = datas[i].split()

        data = [int(x) for x in data]

        valid_differences = all(ecart in {1, 2, 3} for ecart in [data[i+1] - data[i] for i in range(len(data)-1)])
        ascending_order = all(data[i] < data[i+1] for i in range(len(data)-1))
        descending_order = all(data[i] > data[i+1] for i in range(len(data)-1))

        if (ascending_order or descending_order) and valid_differences:
            total_safe_lines += 1

    print(f"Total safe lines: {total_safe_lines}")

find_total_safe_lines()
