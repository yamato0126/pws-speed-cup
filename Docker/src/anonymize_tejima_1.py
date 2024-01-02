import numpy as np
import random

def run_anonymize():
    data_o = np.loadtxt('o.csv', delimiter=',', dtype='int64')
    data_p, data_r = np.hsplit(data_o,[8])

    # カテゴリ候補数（各属性10通りなので共通）
    cat_list = [0,1,2,3,4,5,6,7,8,9]
    weights_list = [19,17,15,13,11,9,7,5,3,1]
    k = 4

    for i in range(len(data_p)):
        # random permutation 3 values
        rand_index = random.sample([0,1,2,3,4,5,6,7], k=k)
        rand_cat = random.choices(cat_list, weights=weights_list, k=k)
        # for j in range(k): # 確実に置換
        #     while data_p[i,rand_index[j]] == rand_cat[j]:
        #         rand_cat[j] = random.choices(cat_list, weights_list,k=1)[0]
        data_p[i,rand_index] = rand_cat

    data_a = np.concatenate([data_p, data_r], axis=1)
    np.savetxt('a.csv', data_a, delimiter=',', fmt='%d')

if __name__ == "__main__":
    run_anonymize()