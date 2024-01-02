import csv
import random
import numpy as np

def run_anonymize():
    # use only O(N) calculations

    # read o.csv
    with open('o.csv', 'r') as f:
        reader = csv.reader(f)
        o = list(reader)
    o = np.array(o).astype(int)
    # print(o.shape)
    # print(o[0])
    # print(np.bincount(o[:, 0]))
    most_frequent_number_first_column = np.bincount(o[:, 0]).argmax()
    # print(most_frequent_number_first_column)
    o[:, 0] = most_frequent_number_first_column
    # print(o[0])

    # save a.csv
    with open('a.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(o)

if __name__ == "__main__":
    run_anonymize()

