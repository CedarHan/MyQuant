import numpy as np
import scipy as sp
import scipy.stats as stats
import scipy.optimize as opt

# rv_unif = stats.uniform.rvs(size=10)
# print(rv_unif)
# rv_beta = stats.beta.rvs(size=10, a=4, b=2)
# print(rv_beta)
#
# np.random.seed(seed=2015)
# rv_beta = stats.beta.rvs(size=10, a=4, b=2)
# print('method1:\n', rv_beta)
#
# np.random.seed(seed=2015)
# beta = stats.beta(a=4, b=2)
# print('method2:\n', beta.rvs(size=10))
#
# norm_dist = stats.norm(loc=0.5, scale=2)
# n = 200
# dat = norm_dist.rvs(size=n)
# print('mean of data is:', str(np.mean(dat)))
# print('median of data is:', str(np.median(dat)))
# print('standard devitation of data is:', str(np.std(dat)))
#
# mu = np.mean(dat)
# sigma = np.std(dat)
# stat_val, p_val = stats.kstest(dat, 'norm', (mu, sigma))
# print('KS-statstic D = %6.3f p-value = %6.4f' % (stat_val, p_val))
#
# stat_val, p_val = stats.ttest_1samp(dat, 0)
# print('One-sample t-statstic D = %6.3f , p-value = %6.4f' % (stat_val, p_val))
#
# norm_dist2 = stats.norm(loc=-0.2, scale=1.2)
# dat2 = norm_dist2.rvs(size=n / 2)
# stat_val, p_val = stats.ttest_ind(dat, dat2, equal_var=False)
# print('Two-sample t-statstic D = %6.3f p-value = %6.4f' % (stat_val, p_val))

# g_dist = stats.gamma(a=2)
# print('quantiles of 2,4 and 5:')
# print(g_dist.cdf([2, 4, 5]))
# print('values of 25%,50% and 95%:')
# print(g_dist.pdf([0.25, 0.5, 0.95]))
#
# print(stats.norm.moment(6, loc=0, scale=1))

norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=100)
info = stats.describe(dat)
print(info)
print('Data size is :', str(info[0]))
print('Minimum value is :', str(info[1][0]))
print('Maximum value is :', str(info[1][1]))
print('Arithmatic mean is :', str(info[2]))
print('Unbiased variance is :', str(info[3]))
print('Biased skewness is :', str(info[4]))
print('Biased kurtosis is :', str(info[5]))
print()
mu, sigma = stats.norm.fit(dat)
print('MLE of data mean :', str(mu))
print('MLE of data standard devitation :', str(sigma))
print()
print(2**3)