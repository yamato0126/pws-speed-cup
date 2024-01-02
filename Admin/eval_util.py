import pandas as pd

from common import calculate_differing_rate


def eval_util(team=None):
    # File paths
    file_path1 = '../Docker/src/o.csv'
    file_path2 = f'../Docker/src/a{team}.csv'
    df1 = pd.read_csv(file_path1, header=None)
    df2 = pd.read_csv(file_path2, header=None)

    # Compute the differing rate
    differing_rate = calculate_differing_rate(df1, df2)
    print(f"utility:{1 - differing_rate}")
    with open(f'../Docker/src/util{team}.txt', 'a') as f:
        print(1 - differing_rate, file=f)


def main():
    team_list = ['_miura_1', '_miura_2', '_miura_3', '_sugiura', '_tejima_1', '_tejima_2', '_base_st', '_base_ut']
    for team in team_list:
        eval_util(team)


if __name__ == '__main__':
    main()
