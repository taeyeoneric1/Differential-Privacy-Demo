import matplotlib.pyplot as plt
import numpy as np

#高斯噪声
def Gaussian_noisy(sensitivety,epsilon,delta):
    sigma = np.sqrt(2*np.log(1.25/delta))*1/epsilon
    n_value = np.random.normal(loc = 0, scale= sigma)
    return n_value


#拉普拉斯差分隐私
def Gaussian_mech(data,sensitivety,epsilon,delta):
    for i in range(len(data)):
        data[i] += Gaussian_noisy(sensitivety,epsilon,delta)
    return data

def avg_attack(query, epsilon, k):
    results = [query + np.random.laplace(loc=0, scale=1/epsilon) for i in range(k)]
    return np.mean(results)

def adv_comp(k, epsilon, delta):
    return 2*epsilon*np.sqrt(2*k*np.log(1/delta))

def seq_comp(k, epsilon):
    return k*epsilon

if __name__ =='__main__':
    # x = [1.,1.,0.]
    # sensitivety = 1
    # epsilon = 1
    # delta = 10e-5
    # data = Gaussian_mech(x,sensitivety,epsilon,delta)
    # for j in data:
    # print(j)
    x = np.linspace(0.01, 0.1, 10)
    print(x)