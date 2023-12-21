import pandas as pd
import numpy as np
from tqdm import tqdm
import collections
import scipy.stats as stats

import cupy as cp # GPUを使用する場合，cupyが必要
# import cupyx.scipy.stats as cp_stats
''' 
実行時間の目安
GPUあり: 20 分
GPUなし: 4 時間
'''

from common import calculate_differing_rate, candidates, candidates_gpu


def hamm_attack(h_min=0, gpu_use=False):
    # パラメータ
    m_p = 8 # 公開部の列数

    # ファイルのパス
    path_o = '../Docker/src/o.csv'
    path_b = '../Docker/src/b.csv'

    # 元データ読み込み
    df_o = pd.read_csv(path_o, sep=',', header=None).astype(int)
    df_o_p = df_o.iloc[:,:m_p] # 元データ公開部
    np_o_p = df_o_p.values
    if gpu_use:
        cp_o_p = cp.asarray(np_o_p)

    # 整列加工データ読み込み
    df_b = pd.read_csv(path_b, sep=',', header=None).replace('*', 10).astype(int) # "*"は10に置換
    df_b_p = df_b.iloc[:,:m_p] # 整列加工データ公開部
    np_b_p = df_b_p.values
    if gpu_use:
        cp_b_p = cp.asarray(np_b_p)

    can_index = [] # ハミング距離最小のインデックスを格納（複数ある場合はランダム）
    ham = [] # ハミング距離を格納
    if gpu_use:
        for cp_o_p_i in tqdm(cp_o_p):
            h = h_min
            while True:
                can = candidates_gpu(h, cp_o_p_i, cp_b_p)
                if len(can) != 0:
                    can_index.append(can)
                    ham.append(h)
                    break
                h += 1
    else:
        for np_o_p_i in tqdm(np_o_p):
            h = h_min
            while True:
                can = candidates(h, np_o_p_i, np_b_p)
                if len(can) != 0:
                    can_index.append(can)
                    ham.append(h)
                    break
                h += 1
    
    c = collections.Counter(ham)
    print(c) # ハミング距離の出現回数を出力

    df_b_r = df_b.iloc[:,m_p:] # 整列加工データ秘密部
    np_b_r = df_b_r.values
    if gpu_use:
        cp_b_r = cp.asarray(np_b_r)

    ans = [] # 秘密推定データを格納
    if gpu_use:
        for idx_list in tqdm(can_index):
            mode_val, mode_num = stats.mode(cp_b_r[idx_list].get(), axis=0)
            ans.append(mode_val)
    else:
        for idx_list in tqdm(can_index):
            mode_val, mode_num = stats.mode(np_b_r[idx_list], axis=0)
            ans.append(mode_val)
    np_ans = np.array(ans)
    df_ans = pd.DataFrame(np_ans)

    # 安全性評価
    df_o_r = df_o.iloc[:,m_p:] # 元データ秘密部
    df_o_r = df_o_r.rename(columns={8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:6, 15:7, 16:8, 17:9})

    differing_rate = calculate_differing_rate(df_ans, df_o_r)
    print(f"safety:{differing_rate}")
    with open('../Docker/src/safe.txt', 'w') as f:
        print(differing_rate, file=f)


def main():
    gpu_use = True # GPUを使用するか
    h_min = 0 # ハミング距離の最小値
    hamm_attack(h_min, gpu_use)


if __name__ == '__main__':
    main()
