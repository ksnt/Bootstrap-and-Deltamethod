#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bootstrap and Delta-method program                                           
# Author: Takayuki Kaisen

import numpy as np

S = float(1000.0000)
dm_result = [] # Result of Delta method
bs_result = [] # Result of Bootstrap method

def main(n):
    n = int(n)
    for s in range(int(S)):
        x = np.random.uniform(0,1,n) # n個の乱数列はS回つくる
        dm_result.append(delta(x,n))
        bs_result.append(boot(x,n))
    print("Result of Delta-method is : %f" % (np.sum(dm_result)/S) )# T(成功回数)/S(試行回数)を計算してその割合を表示
    print("Result of Bootstrap-method is : %f" % (np.sum(bs_result)/S) )# T(成功回数)/S(試行回数)を計算してその割合を表示
    return 0

# Delta method
def delta(x,n):                                               
    upper_bound = 1/np.mean(x) + (1.96/np.sqrt(n))*2/np.sqrt(3)
    lower_bound = 1/np.mean(x) - (1.96/np.sqrt(n))*2/np.sqrt(3)
    return [(0,1) [lower_bound <= 2 <= upper_bound]]

# Bootstrap method          
def boot(x,n):
    """1.重複を許してsub-samplingを行う
       2.sub-samplingに対してg(theta)を計算する
       3.得られたg(theta)をソートする
       4.ソート結果の下位2.5%番目と上位2.5%番目までの間に2が入っているかどうか判定する.Trueなら1を，Falseなら0を返すようにする.
         0か1を返り値とする.
    """
    g_theta_list = []
    #T=10000
    T = 1000
    for t in range(T):
        new_x_list = []
        [new_x_list.append(x[i]) for i in map(int,map(np.floor,np.random.uniform(0,n,n)))]
        g_theta_list.append(1/np.mean(new_x_list))
    g_theta_list.sort()
    lower_bound = g_theta_list[24]
    upper_bound = g_theta_list[974]
    return [(0,1) [lower_bound <= 2 <= upper_bound]]

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 2:
        n = args[1]
    else:
        print("The number of given arguments is wrong. \nYou should give one argument.\n")
        sys.exit()
    main(n)
