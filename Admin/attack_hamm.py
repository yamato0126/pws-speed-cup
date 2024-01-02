import pandas as pd
import numpy as np
from tqdm import tqdm
import collections

import cupy as cp # GPUを使用する場合，cupyが必要
''' 
実行時間の目安
GPUあり: 8 分
GPUなし: 4 時間
'''

from common import calculate_differing_rate, candidates, candidates_gpu


def hamm_attack(h_min=0, gpu_use=False, team=None):
    # パラメータ
    m_p = 8 # 公開部の列数

    # ファイルのパス
    path_o = '../Docker/src/o.csv'
    path_b = f'../Docker/src/b{team}.csv'

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
                    idx = np.random.randint(0, len(can)) 
                    can_index.append(can[idx])
                    ham.append(h)
                    break
                h += 1
    else:
        for np_o_p_i in tqdm(np_o_p):
            h = h_min
            while True:
                can = candidates(h, np_o_p_i, np_b_p)
                if len(can) != 0:
                    idx = np.random.randint(0, len(can)) 
                    can_index.append(can[idx])
                    ham.append(h)
                    break
                h += 1
    
    c = collections.Counter(ham)
    print(c) # ハミング距離の出現回数を出力

    df_b_r = df_b.iloc[:,m_p:] # 整列加工データ秘密部
    np_b_r = df_b_r.values
    if gpu_use:
        cp_b_r = cp.asarray(np_b_r)

    # 秘密推定データを格納
    if gpu_use:
        np_ans = cp_b_r[can_index].get()
    else:
        np_ans = np_b_r[can_index]
    df_ans = pd.DataFrame(np_ans)

    # 安全性評価
    df_o_r = df_o.iloc[:,m_p:] # 元データ秘密部
    df_o_r = df_o_r.rename(columns={8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:6, 15:7, 16:8, 17:9})

    differing_rate = calculate_differing_rate(df_ans, df_o_r)
    print(f"safety:{differing_rate}")
    with open(f'../Docker/src/safe{team}.txt', 'a') as f:
        print(h_min, file=f)
        print(differing_rate, file=f)


def main():
    gpu_use = True # GPUを使用するか
    team_list = ['_miura_1', '_miura_2', '_miura_3', '_sugiura', '_tejima_1', '_tejima_2', '_base_st', '_base_ut']
    h_min_list = [3, 3, 3, 1, 3, 3, 3, 0]
    for team, h_min in zip(team_list, h_min_list):
        for i in range(h_min+1):
            hamm_attack(i, gpu_use, team)


if __name__ == '__main__':
    main()
