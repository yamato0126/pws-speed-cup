import time
import numpy as np
import anonymize_miura_1 as anonymize # 実行する匿名化プログラムを指定

def main():
    '''
    匿名化処理実行時間計測.
    匿名化処理を10回行い、その平均実行時間を計測する. 
    Anonymization process execution time measurement.
    Measure the average execution time of 10 times anonymization process.
    '''
    exp_num = 10
    total_time = 0
    time_list = []
    
    for i in range(exp_num):
        start_time = time.perf_counter()
        anonymize.run_anonymize()
        end_time = time.perf_counter()

        exe_time = end_time - start_time
        print(f'execution time is {exe_time}')
        total_time += exe_time
        time_list.append(exe_time)

    print(f'average execution time is {total_time/exp_num}')
    with open('time.txt', 'w') as f:
        print(total_time/exp_num, file=f)
        print(np.std(np.array(time_list), ddof=1), file=f)
    print('Perfect!!!')

if __name__ == "__main__":
    main()