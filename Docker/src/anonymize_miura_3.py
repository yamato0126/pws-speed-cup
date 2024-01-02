import pandas as pd
import random

def run_anonymize():
    # 読み込み
    df_o = pd.read_csv("o.csv",header=None)

    # 処理
    K=3
    for i in range(len(df_o)//2):
        rand_ind = random.sample([0,1,2,3,4,5,6,7],k=K)
        # rand_cat = random.choices([0,1,2,3,4,5,6,7,8,9], k=K)
        tmp = df_o.iloc[i,rand_ind]
        df_o.iloc[i,rand_ind] = df_o.iloc[i+500000,rand_ind]
        df_o.iloc[i+500000,rand_ind] = tmp

    # 書き出し
    df_o.to_csv("a.csv",header=False, index=False)

if __name__ == "__main__":
    run_anonymize()


