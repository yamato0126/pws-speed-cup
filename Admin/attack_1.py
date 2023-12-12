import pandas as pd
import numpy as np
from tqdm import tqdm
import collections

from common import calculate_differing_rate

def hamm_dis(record, np_records):    
    ''' 
    ハミング距離計算する
    '''
    distances = (np_records != record).sum(axis=1)
    return distances

def candidates(h, record, np_records):
    '''
    ハミング距離がhのもののインデックスをリストで返す
    record(一つのレコード)とnp_records(レコードの集まり)とのハミング距離を計算し,
    np_records 内のハミング距離がh のレコードのインデックスを返す
    '''
    dis = hamm_dis(record, np_records)
    return list(np.where(dis == h)[0])

def main(h_min):
    # パラメータ
    m_p = 8 # 公開部の列数

    # ファイルのパス
    path_o = '../Docker/src/o.csv'
    path_b = '../Docker/src/b.csv'

    # 元データ読み込み
    df_o = pd.read_csv(path_o, sep=',', header=None).astype(int)
    df_o_p = df_o.iloc[:,:m_p] # 元データ公開部
    np_o_p = df_o_p.values

    # 整列加工データ読み込み
    df_b = pd.read_csv(path_b, sep=',', header=None).replace('*', 10).astype(int) # "*"は10に置換
    df_b_p = df_b.iloc[:,:m_p] # 整列加工データ公開部
    np_b_p = df_b_p.values

    can_index = [] # ハミング距離最小のインデックスを格納（複数ある場合はランダム）
    ham = [] # ハミング距離を格納
    for i in tqdm(range(np_o_p.shape[0])):
        h = h_min
        while True:
            can = candidates(h, np_o_p[i], np_b_p)
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

    ans = [] # 秘密推定データを格納
    for i in range(len(can_index)):
        ans.append(np_b_r[can_index[i]])
    np_ans = np.array(ans)
    df_ans = pd.DataFrame(np_ans)

    # 安全性評価
    df_o_r = df_o.iloc[:,m_p:] # 元データ秘密部
    df_o_r = df_o_r.rename(columns={8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:6, 15:7, 16:8, 17:9})

    differing_rate = calculate_differing_rate(df_ans, df_o_r)
    print(f"safety:{differing_rate}")
    with open('../Docker/src/safe.txt', 'w') as f:
        print(differing_rate, file=f)

if __name__ == '__main__':
    # 最小距離0のハミングマッチング攻撃
    main(h_min=0)