# pandas - data clenning
# csv - comma separated files


import pandas as pd


# s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

# print(s[2])

# data = {
#     'Country': ['Belgium', 'India', 'Brazil'],
#     'Capital': ['Brussels', 'New Delhi', 'Brasília'],
#     'Population': [11190846, 1303171035, 207847528]
# }

# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("dirtydata.csv")

# print(df.to_string())

# df = pd.read_json("opendata.json")

# print(df.info())

# df = pd.read_csv("dirtydata.csv")

# x = df.dropna()
# print(df)
# df.dropna(inplace=True)
# print(df)

# df.fillna(1300, inplace=True)
# print(df)

# Data cleaning using pandas
# replace - mean(), medaian(), mode()

""" mean() """

# df = pd.read_csv("dirtydata.csv")

# x = df.mean()

# df.fillna(x, inplace=True)

# print(df)

""" medaian() """
# df = pd.read_csv("dirtydata.csv")

# x = df.median()

# df.fillna(x, inplace=True)

# print(df)

"""mode()"""
# df = pd.read_csv("dirtydata.csv")

# x = df["Calories"].mode()[0]

# df["Calories"].fillna(x, inplace=True)

# print(df.to_string())

"""Cleaning wrong format """

# df = pd.read_csv("dirtydata.csv")

# df["Date"] = pd.to_datetime(df["Date"])
# df.dropna(subset=["Date"], inplace=True)
# df.dropna(subset=["Calories"], inplace=True)
# print(df.to_string())

""" same particular value change """

# df = pd.read_csv("dirtydata.csv")

# df.loc[7, "Duration"] = 120

# print(df.to_string)

# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] = 120
# print(df)

# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.drop(x, inplace=True) 
# print(df)

"""Removing Duplicates datas"""

df = pd.read_csv("dirtydata.csv")

# x = df.duplicated()
# print(x)

df.drop_duplicates(inplace=True)
print(df)

import pandas as pd

# df = pd.read_csv("dirtydata.csv")
# df.fillna(1300, inplace=True)

# print(df)

""" hoe to save csv file in pandas """
# df = pd.read_csv("dirtydata.csv")
# df.fillna(1300, inplace=True)

# print(df)

# df.to_csv("file.csv")
# df.to_json("file.json")

""" data correlation - corr() """
# -1 to 1 (0.5 - 0.9)

df = pd.read_csv("dirtydata.csv")

print(df.corr())


"""plotting - plot()"""

import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.plot()

plt.show()


