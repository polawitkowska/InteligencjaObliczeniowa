import pandas as pd

df = pd.read_csv("./lab02/iris_with_errors.csv")

numbers_df = df.values[:, 0:4]
names_df = df.values[:, -1]

def count_empty(data):
    minus = 0
    nan = 0
    zero = 0

    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == "-":
                minus += 1
                data[i][j] = 0
            elif pd.isna(item):
                nan += 1
                data[i][j] = 0
            elif item == "0":
                zero += 1
    return minus, nan, zero, data

stats = count_empty(numbers_df)
# print("Items that are '-':", stats[0], "Items that are not a number:", stats[1], "Items that are '0':", stats[2])
numbers_fixed_empty = stats[3]

def replace_out_of_range(data):
    col_sums = [0] * len(data[0])
    col_counts = [0] * len(data[0])
    
    for row in data:
        for j, item in enumerate(row):
            if isinstance(item, str):
                item = float(item)
            if 0 <= float(item) <= 15:
                col_sums[j] += float(item)
                col_counts[j] += 1
    
    col_avgs = [col_sums[j]/col_counts[j] for j in range(len(data[0]))]
    
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if isinstance(item, str):
                data[i][j] = float(item)
            if float(data[i][j]) < 0 or float(data[i][j]) > 15:
                data[i][j] = round(col_avgs[j], 1)
    
    return data

numbers_replaced = replace_out_of_range(numbers_fixed_empty)
# print(numbers_replaced)

def replace_names(data):
    for i, item in enumerate(data):
        if item[0] in ['s', 'v']:
            data[i] = item[0].upper() + item[1:]
        
        if item == 'Versicolour':
            data[i] = 'Versicolor'
    return data

names_fixed = replace_names(names_df)

def rejoin_data(numbers, names):
    numbers_list = numbers.tolist()
    for i, row in enumerate(numbers_list):
        numbers_list[i] = row + [names[i]]
    return numbers_list

data_fixed = rejoin_data(numbers_replaced, names_fixed)
for row in data_fixed:
    print(row)