import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import pandas as pd
import numpy as np

adult = pd.read_csv("adult_with_pii.csv")


def laplace_mech(v, sensitivity, epsilon):
    return v + np.random.laplace(loc=0, scale=sensitivity / epsilon)


def pct_error(orig, priv):
    return np.abs(orig - priv) / orig * 100.0

options = adult['Marital Status'].unique()  # 人口普查中婚姻情况的种类

def score(data, option):
    return data.value_counts()[option]/1000

def exponential(x, R, u, sensitivity, epsilon):
    # 计算R中每个回复的分数
    scores = [u(x, r) for r in R]

    # 根据分数计算每个回复的输出概率
    probabilities = [np.exp(epsilon * score / (2 * sensitivity)) for score in scores]

    # 对概率进行归一化处理，使概率和等于1
    probabilities = probabilities / np.linalg.norm(probabilities, ord=1)

    # 根据概率分布选择回复结果
    return np.random.choice(R, 1, p=probabilities)[0]

r = [exponential(adult['Marital Status'], options, score, 1, 1) for i in range(200)]
pd.Series(r).value_counts()


exponential(adult['Marital Status'], options, score, 1, 1)