import sys
import numpy as np
import random as rd


def loadfile(file_path):
    fil = open(file_path)
    lines = fil.readlines()
    num = len(lines)

    X = np.zeros((num, 5))
    Y = np.zeros((num, 1))

    index = 0
    for line in lines:
        items = line.strip().split('\t')
        X[index][1:5] = np.array([float(i)
                                  for i in items[0].strip().split()])[:]
        X[index][0] = 1
        Y[index][0] = float(items[1])
        index += 1
    return X, Y


def pla_error_rate(features, labels, w):
    length = len(features)
    wrong = 0
    for i in range(length):
        if labels[i][0] * (np.dot(features[i], w))[0] <= 0:
            wrong += 1
    return float(wrong)/float(length)


def pla_pocket(features, labels, index_array, max_times, rate=1):
    w = np.zeros((5, 1))
    w_pocket = np.zeros((5, 1))
    num = len(features)
    flag = 1
    index = 0
    count = 0
    while(flag):
        features_index = index_array[index]
        if labels[features_index][0] * np.dot(features[features_index], w)[0] <= 0:
            w = w + labels[features_index][0] * rate * \
                np.mat(features[features_index]).T
            count += 1
            if pla_error_rate(features, labels, w) < pla_error_rate(features, labels, w_pocket):
                w_pocket = w

        if count >= max_times:
            flag = 0
        elif index >= num - 1:
            index = 0
        else:
            index += 1
    return w, w_pocket


def pla(features, labels, rate=1):
    w = np.zeros((5, 1))
    num = len(features)
    flag = 1
    index = 0
    good_items = 0
    count = 0
    while(flag):
        if labels[index][0] * np.dot(features[index], w)[0] <= 0:
            w = w + labels[index][0] * rate * np.mat(features[index]).T
            good_items = 0
            count += 1
        else:
            good_items += 1

        if good_items >= num:
            flag = 0
        elif index >= num - 1:
            index = 0
        else:
            index += 1
    return count


def pla_fix(features, labels, index_array, rate=1):
    w = np.zeros((5, 1))
    num = len(features)
    flag = 1
    index = 0
    good_items = 0
    count = 0
    while(flag):
        features_index = index_array[index]
        if labels[features_index][0] * np.dot(features[features_index], w)[0] <= 0:
            w = w + labels[features_index][0] * rate * \
                np.mat(features[features_index]).T
            good_items = 0
            count += 1
        else:
            good_items += 1

        if good_items >= num:
            flag = 0
        elif index >= num - 1:
            index = 0
        else:
            index += 1
    return count


if __name__ == '__main__':
    # homework0 15
    (X, Y) = loadfile("q15.txt")
    for x in X:
        print(x)
    # print(pla(X, Y))
    """

    """
    # homework0 16
    """
    (X,Y) = loadfile('data.txt')
    update_array = []
    for i in range(2000):
        index_array = [j for j in range(400)]
        rd.shuffle(index_array)
        tmp = pla_fix(X, Y, index_array)
        update_array.append(tmp)
    print(np.mean(update_array))
    """
    # homework0 17
    """
    (X,Y) = loadfile('data.txt')
    update_array = []
    for i in range(200):
        index_array = [j for j in range(400)]
        rd.shuffle(index_array)
        tmp = pla_fix(X, Y, index_array, rate = 0.5)
        update_array.append(tmp)
    print(update_array)
    """
    # homework0 18
    # (X, Y) = loadfile('pocket_data.txt')
    # (X_test, Y_test) = loadfile('pocket_test.txt')
    # error_rate_array = []
    # for i in range(200):
    #     index_array = [j for j in range(len(X))]
    #     rd.shuffle(index_array)
    #     (w, w_100) = pla_pocket(X, Y, index_array, 100)

    #     error_rate_array.append(pla_error_rate(X_test, Y_test, w_100))
    # print(np.mean(error_rate_array))
