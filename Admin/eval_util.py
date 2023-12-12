import pandas as pd

from common import calculate_differing_rate

# File paths
file_path1 = '../Docker/src/o.csv'
file_path2 = '../Docker/src/a.csv'
df1 = pd.read_csv(file_path1, header=None)
df2 = pd.read_csv(file_path2, header=None)

# Compute the differing rate
differing_rate = calculate_differing_rate(df1, df2)
print(f"utility:{1 - differing_rate}")
with open('../Docker/src/util.txt', 'w') as f:
    print(1 - differing_rate, file=f)
