import numpy as np

def eps2p(epsilon, n=2):
    return np.e ** epsilon / (np.e ** epsilon + n - 1)

def discretization(value, lower=0, upper=1):
    if value > upper or value < lower:
        raise Exception("the range of value is not valid in Function @Func: discretization")

    p = (value - lower) / (upper - lower)
    rnd = np.random.random()
    return upper if rnd < p else lower

def Generate_random_responce(seed):
    """
    :param seed:
    :return:
    """


def random_response(bit_array: np.ndarray, p, q=None):
    """
    :param bit_array:
    :param p: probability of 1->1
    :param q: probability of 0->1
    :return:
    """
    q = 1-p if q is None else q
    # 类型检查
    # 如果bit_array是一个标量的int，那么这个isinstance(bit_array, int)就为真，
    # 但是传入的一个一维的数组，这判断就为假，直接执行后面的return
    if isinstance(bit_array, int):
        probability = p if bit_array == 1 else q
        return np.random.binomial(n=1, p=probability)
    return np.where(bit_array == 1, np.random.binomial(1, p, len(bit_array)), np.random.binomial(1, q, len(bit_array)))


def discretization(value, lower=0, upper=1):
    if value > upper or value < lower:
        raise Exception("the range of value is not valid in Function @Func: discretization")

    p = (value - lower) / (upper - lower)
    rnd = np.random.random()
    return upper if rnd < p else lower

def random_response_adjust(s: np.ndarray, data_len, prob):
    """
    对random response的结果进行校正
    :param s: 收到数据中1的个数,观察到的1的总数
    :param data_len: 总的数据个数，样本个数
    :param prob: eps2p()
    :return: 估计实际中1的个数
    """
    return (s + prob * data_len - data_len) / (2 * prob - 1)


# 返回value值，或返回values中的非value值
def k_random_response(value, values, epsilon):
    """
    the k-random response
    :param value: current value
    :param values: the possible value
    :param epsilon: privacy budget
    :return:
    """
    if not isinstance(values, list):
        raise Exception("The values should be list")
    if value not in values:
        raise Exception("Errors in k-random response")
    p = np.e ** epsilon / (np.e ** epsilon + len(values) - 1)
    if np.random.random() < p:  # p是一个大于1/2概率的值
        return value
    values.remove(value)  # 将value移除
    return values[np.random.randint(low=0, high=len(values))]  # 返回values中任意一个非value的值




