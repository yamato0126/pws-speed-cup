# import pandas as pd
# import numpy as np
import csv
# import time

def run_anonymize():
    # start_time = time.perf_counter()
    # df = pd.read_csv('o.csv', header=None)
    # data_o = np.loadtxt('o.csv', delimiter=',', dtype='int64')
    with open('o.csv', 'r') as f:
        reader = csv.reader(f)
        o = list(reader)
    # end_time = time.perf_counter()
    # print(f'read time is {end_time - start_time}')

    # start_time = time.perf_counter()
    # df.to_csv('a.csv', header=False, index=False)
    # np.savetxt('a.csv', data_o, delimiter=',', fmt='%d')
    with open('a.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(o)
    # end_time = time.perf_counter()
    # print(f'write time is {end_time - start_time}')

if __name__ == "__main__":
    run_anonymize()