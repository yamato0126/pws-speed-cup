def calculate_differing_rate(df_1, df_2):
    # Ensure the dimensions match
    if df_1.shape != df_2.shape:
        raise ValueError("CSV files have different dimensions")

    # Count the number of differing elements
    differing_elements_count = (df_1 != df_2).sum().sum()

    # Calculate the total number of elements
    total_elements = df_1.shape[0] * df_1.shape[1]

    # Calculate the differing rate
    differing_rate = (differing_elements_count / total_elements)

    return differing_rate


def hamm_dis(record, np_records):    
    ''' 
    ハミング距離を計算する
    '''
    distances = (np_records != record).sum(axis=1)
    return distances


def candidates(h, record, np_records):
    '''
    record(単一レコード)とnp_records(レコード集合)のハミング距離を計算し，
    ハミング距離がhのレコードのインデックスのリストを返す
    '''
    import numpy as np

    dis = hamm_dis(record, np_records)
    return list(np.where(dis == h)[0])


def candidates_gpu(h, record, np_records):
    import cupy as cp

    dis = hamm_dis(record, np_records)
    return list(cp.where(dis == h)[0])
