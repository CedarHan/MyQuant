# 基于Black - Scholes 公式的期权定价公式
from math import log, sqrt, exp
from scipy.stats import norm
import time
import numpy as np
from matplotlib import pylab
import seaborn as sns


# from CAL.PyCAL import *

def call_option_pricer(spot, strike, maturity, r, vol):
    d1 = (log(spot / strike) + (r + 0.5 * vol * vol) * maturity) / vol / sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)

    price = spot * norm.cdf(d1) - strike * exp(-r * maturity) * norm.cdf(d2)
    return price


# 参数
spot = 2.45
strike = 2.50
maturity = 0.25
r = 0.05
vol = 0.25

print('期权价格：%.4f' % call_option_pricer(spot, strike, maturity, r, vol))

portfolioSize = range(1, 10000, 500)
timeSpent = []

for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0, 3.0, size)
    for i in range(size):
        res = call_option_pricer(spot, strikes[i], maturity, r, vol)
    timeSpent.append(time.time() - now)

# font.set_size(15)
sns.set(style="ticks")
pylab.figure(figsize=(12, 8))
pylab.bar(portfolioSize, timeSpent, color='r', width=300)
pylab.grid(True)
pylab.title(u'期权计算时间耗时（单位：秒）', fontsize=18)
pylab.ylabel(u'时间（s)', fontsize=15)
pylab.xlabel(u'组合数量', fontsize=15)

# https://uqer.io/community/share/5514fc98f9f06c8f33904449
# 量化分析师的Python日记【第7天：Q Quant 之初出江湖】
