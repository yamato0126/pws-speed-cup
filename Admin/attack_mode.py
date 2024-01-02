import pandas as pd
import numpy as np
from scipy import stats

from common import calculate_differing_rate


def mode_attack(team=None):
    # パラメータ
    m_p = 8 # 公開部の列数

    # ファイルのパス
    path_o = '../Docker/src/o.csv'
    path_b = f'../Docker/src/b{team}.csv'

    # 元データ読み込み
    df_o = pd.read_csv(path_o, sep=',', header=None).astype(int)

    # 整列加工データ読み込み
    df_b = pd.read_csv(path_b, sep=',', header=None).replace('*', 10).astype(int) # "*"は10に置換
    df_b_r = df_b.iloc[:,m_p:] # 整列加工データ秘密部
    np_b_r = df_b_r.values
    
    mode_value = stats.mode(np_b_r, axis=None).mode
    print(f"mode:{mode_value}")

    # 秘密推定データを格納
    np_ans = np.full_like(np_b_r, mode_value)
    df_ans = pd.DataFrame(np_ans)

    # 安全性評価
    df_o_r = df_o.iloc[:,m_p:] # 元データ秘密部
    df_o_r = df_o_r.rename(columns={8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:6, 15:7, 16:8, 17:9})

    differing_rate = calculate_differing_rate(df_ans, df_o_r)
    print(f"safety:{differing_rate}")
    with open(f'../Docker/src/safe{team}.txt', 'a') as f:
        print("mode", file=f)
        print(differing_rate, file=f)


def main():
    team_list = ['_miura_1', '_miura_2', '_miura_3', '_sugiura', '_tejima_1', '_tejima_2', '_base_st', '_base_ut']
    for team in team_list:
        mode_attack(team)


if __name__ == '__main__':
    main()