import pandas as pd

def run_anonymize():
    # 読み込み
    df_o = pd.read_csv("o.csv",header=None)

    # 処理
    df_o.iloc[:250000,[1,3,5,7]] = 0
    df_o.iloc[250000:500000,[0,2,4,6]] = 0
    df_o.iloc[500000:750000,[1,2,5,6]] = 0
    df_o.iloc[750000:,[0,3,4,7]] = 0

    # 書き出し
    df_o.to_csv("a.csv",header=False, index=False)

if __name__ == "__main__":
    run_anonymize()

