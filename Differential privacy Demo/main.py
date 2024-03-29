from DP_mechanism import ExponentiationDP, GaussianDP, LaplaceDP, BernoulliDP
import pandas as pd
import numpy as np

if __name__ == '__main__' :
    DP  = ['Laplace' ,'Gaussian' ,'Exponentiation' ,'Bernoulli']
    task_id =0
    if DP[task_id] == 'Laplace':
        x = [1., 1., 0.]
        sensitivety = 1
        epsilon = 1
        data = LaplaceDP.laplace_mech(x, sensitivety, epsilon)
        for j in data:
            print(j)

    elif DP[task_id] == 'Gaussian':
        x = [1., 1., 0.]
        sensitivety = 1
        epsilon = 1
        delta = 10e-5
        data = GaussianDP.Gaussian_mech(x,sensitivety,epsilon,delta)
        for j in data:
            print(j)

    elif DP[task_id] == 'Exponentiation':
        data = pd.read_csv("adult_with_pii.csv")
        options = data['Marital Status'].unique()
        r = [ExponentiationDP.exponential(data['Marital Status'], options, ExponentiationDP.score(data, options), 1, 1) for i in range(200)]
        pd.Series(r).value_counts()

        ExponentiationDP.exponential(data['Marital Status'], options,  ExponentiationDP.score(data, options), 1, 1)

    elif DP[task_id] == 'Bernoulli':
        epsilon = 1
        data = pd.read_csv("random_choice.csv")
        data = BernoulliDP.random_response(data, 0.5 ,0.5)
        data = BernoulliDP.random_response_adjust(data, 100, BernoulliDP.eps2p(epsilon, n=2))
        