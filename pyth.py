import numpy as np
from scipy.stats import triang, lognorm, pareto

# Parameters
a, b, c = 10000, 35000, 18000
point1, point2 = 12000, 25000
mu, sigma, xm, alpha = 0, 3, 1, 4
num = 500000
point3, point4, point5 = 30, 50, 100
data = [11, 15, 9, 5, 3, 14, 16, 15, 12, 10, 11, 4, 7, 12, 6]

def Task1(a, b, c, point1, point2, data, mu, sigma, xm, alpha, num, point3, point4, point5):
    # Probability that the AV is no greater than point1
    dist = triang(c=(c-a)/(b-a), loc=a, scale=b-a)
    prob1 = dist.cdf(point1)
    
    # Probability that the AV is greater than point2
    prob2 = 1 - dist.cdf(point2)
    
    # Mean and median of the AV
    MEAN_t = dist.mean()
    MEDIAN_t = dist.median()
    
    # Mean and variance of the data set
    MEAN_d = np.mean(data)
    VARIANCE_d = np.var(data, ddof=1)
    
    # Probability that the total impact is greater than point3
    sample_A = lognorm(s=sigma, loc=0, scale=np.exp(mu)).rvs(num)
    sample_B = pareto(b=alpha, loc=0, scale=xm).rvs(num)
    total_impact = sample_A + sample_B
    prob3 = np.mean(total_impact > point3)
    
    # Probability that the total impact is between point4 and point5
    prob4 = np.mean(np.logical_and(total_impact >= point4, total_impact <= point5))
    
    # Value of the ALE
    SLE = MEDIAN_t * prob3
    ALE = MEAN_d * SLE
    
    return (prob1, prob2, MEAN_t, MEDIAN_t, MEAN_d, VARIANCE_d, prob3, prob4, ALE)

results = Task1(a, b, c, point1, point2, data, mu, sigma, xm, alpha, num, point3, point4, point5)
print(results)
