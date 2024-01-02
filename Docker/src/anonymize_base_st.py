import pandas as pd

def run_anonymize():
    df = pd.read_csv('o.csv', header=None)
    
    df.iloc[:,[0,1,2,3,4,5,6,7]] = 0

    df.to_csv('a.csv', header=False, index=False)

if __name__ == "__main__":
    run_anonymize()