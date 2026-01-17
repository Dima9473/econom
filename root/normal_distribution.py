import numpy as np
from scipy import stats

# для нормализованного нормального распределения - то есть mu = 0 и sigma = 1
# print(stats.norm.pdf(0.0))
# print(stats.norm.cdf(3 / 5) - stats.norm.cdf(-3 / 5))
# print(stats.norm.ppf(0.1))
# print(stats.norm.rvs(size=10))
# print(stats.norm.mean())
# print(stats.norm.std())
# print(stats.norm.__repr__())

# 3 это значение, 5 это число степеней свободы
# print(stats.chi2.cdf(3, 5))  # chi2.cdf(x, df)
# print(stats.chi2.ppf(0.95, 3))  # chi2.ppf(q, df)


# print(stats.t.cdf(3, 2))  # t.cdf(x, df)

# print(stats.t.cdf(4, 2) - stats.t.cdf(3, 2))

# квантиль t-распределения
# a = [0.1, 0.3, 0.5, 0.7, 0.9]
# print(stats.t.ppf(a, 2))


# print(stats.f.cdf(3, 5, 2))  # f.cdf(x, dfn, dfd)
# print(stats.f.cdf(4, 2, 5) - stats.f.cdf(3, 2, 5))

# квантиль t-распределения
# a = [0.1, 0.3, 0.5, 0.7, 0.9]
# print(stats.f.ppf(a, 2, 5))
# print(stats.f.ppf(0.95, 2, 3))  # f.ppf(q, dfn, dfd)


# print(stats.binom.cdf(3, 10, 0.5))  # binom.cdf(k, n, p)
# print(stats.binom.ppf(0.95, 10, 0.5))  # binom.ppf(q, n, p)

np.random.normal(0, 2)
print(np.mean(np.random.normal(0, 2, 20)))
