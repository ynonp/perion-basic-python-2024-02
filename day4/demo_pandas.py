import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("data/train.csv", delimiter='|')
    df.groupby('shana')["sivug_rashi_count"].sum().plot()
    plt.show()