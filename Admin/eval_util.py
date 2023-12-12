import pandas as pd

def compare_csv_files(file_path1, file_path2):
    # Read the CSV files
    df1 = pd.read_csv(file_path1, header=None)
    df2 = pd.read_csv(file_path2, header=None)

    # Ensure the dimensions match
    if df1.shape != df2.shape:
        raise ValueError("CSV files have different dimensions")

    # Count the number of differing elements
    differing_elements_count = (df1 != df2).sum().sum()

    # Calculate the total number of elements
    total_elements = df1.shape[0] * df1.shape[1]

    # Calculate the differing rate
    differing_rate = (differing_elements_count / total_elements)

    return differing_rate

# File paths
file_path1 = '../Docker/src/o.csv'
file_path2 = '../Docker/src/a.csv'

# Compute the differing rate
differing_rate = compare_csv_files(file_path1, file_path2)
print(f"utility:{1 - differing_rate}")
with open('../Docker/src/util.txt', 'w') as f:
    print(1 - differing_rate, file=f)
