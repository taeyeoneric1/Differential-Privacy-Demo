import matplotlib.pyplot as plt
import numpy as np

#拉普拉斯噪声
def laplace_noisy(sensitivety,epsilon):
    n_value = np.random.laplace(0, sensitivety/epsilon, 1)
    return n_value

#隐私量
def noisyCount(sensitivety,epsilon):
    beta = sensitivety/epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta*np.log(1.-u2)
    else:
        n_value = beta*np.log(u2)
    print(n_value)
    return n_value

#拉普拉斯差分隐私
def laplace_mech(data,sensitivety,epsilon):
    for i in range(len(data)):
        data[i] += noisyCount(sensitivety,epsilon)
    return data

#拉普拉斯机制满足ϵ-差分隐私
if __name__ =='__main__':
    x = [1.,1.,0.]
    sensitivety = 1
    epsilon = 1
    data = laplace_mech(x,sensitivety,epsilon)
    for j in data:
        print(j)