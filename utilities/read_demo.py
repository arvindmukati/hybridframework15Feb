"""This will be not a part of framework"""

import pandas
df = pandas.read_csv(filepath_or_buffer="../test_data/test_employee_data.csv",delimiter=";")
print(df)
print(df.loc[0])
print(list(df.loc[0]))
print(tuple(df.loc[0]))
print(df.loc[1].tolist())
print(df.index)
list1 = []
for i in df.index:
    print(df.loc[i].tolist())

print(df.values.tolist())

df1 = pandas.read_json(path_or_buf="../test_data/Data.json",typ=dict)
print(df1)