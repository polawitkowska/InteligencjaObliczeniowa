import pandas as pd

df = pd.read_csv("./lab02/iris_with_errors.csv")

numbers_df = df.values[:, 0:4]

def count_empty(data):
    minus = 0
    nan = 0
    zero = 0

    for row in data:
        for item in row:
            if item == "-":
                minus += 1
            elif pd.isna(item):
                nan += 1
            elif  item == "0":
                zero += 1
    return minus, nan, zero

stats = count_empty(numbers_df)
print("Items that are '-': ", stats[0], "Items that are 'nan': ", stats[1], "Items that are '0': ", stats[2])