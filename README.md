# Python

Calculation of annualized loss expectancy

The annualized loss expectancy (ALE) is an important metric to quantify the exposure of an
asset caused by certain risks. It is equal to the product of the annual rate of occurrence (ARO)
and the single loss expectancy (SLE). The ARO is an estimate of how often a risk would be
successful in exploiting a vulnerability. The SLE is the monetary value expected from the
occurrence of a risk on an asset and it is equal to the product of the typical asset value (AV)
and the exposure factor (EF), where the EF represents the impact of the risk over the asset or
percentage of asset lost. In conclusion of the above, we have the following two relationships:
ALE = ARO × SLE (Eq. 1)
SLE = AV × EF (Eq. 2)
(1) Consider a specific cyber risk on an asset. Assume that the AV follows a triangular
distribution with lower limit 𝒂 = £10000, upper limit 𝒃 = £35000, and mode 𝒄 =
£18000.
(i) Find the probability 𝐩𝐫𝐨𝐛𝟏 that the AV is no greater than 𝐩𝐨𝐢𝐧𝐭𝟏 = £12000.
(ii) Find the probability 𝐩𝐫𝐨𝐛𝟐 that the AV is greater than 𝐩𝐨𝐢𝐧𝐭𝟐 = £25000.
(iii) Find the mean 𝐌𝐄𝐀𝐍_𝐭 and median 𝐌𝐄𝐃𝐈𝐀𝐍_𝐭 of the AV.
(2) We have collected the numbers of annual occurrences of the cyber risk for 15 years,
given by the data set 𝐝𝐚𝐭𝐚 = (11, 15, 9, 5, 3, 14, 16, 15, 12, 10, 11, 4, 7, 12, 6) .
Calculate the mean 𝐌𝐄𝐀𝐍_𝐝 and variance 𝐕𝐀𝐑𝐈𝐀𝐍𝐂𝐄_𝐝 of the data set.
(3) The Monte Carlo method has been widely used in risk analysis to generate draws from
a probability distribution. It relies on repeated random sampling to obtain numerical
results. Suppose that two flaws, A and B, are considered in the above problem. Each
flaw will cause certain amount of impact. In particular, the impact caused by flaw A
follows the log-normal distribution with 𝝁 = 0 and 𝝈 = 3. The impact caused by flaw
B follows the Pareto distribution with 𝒙𝒎 = 1 and 𝜶 = 4. The total impact is the sum
of the impacts caused by the two flaws. Use Monte Carlo method to simulate the
probability distribution of the total impact. Specifically:
(i) Randomly sample 𝐧𝐮𝐦 = 500000 points for the total impact.
(ii) Based on your sampling points, derive the probability 𝐩𝐫𝐨𝐛𝟑 that the total
impact is greater than 𝐩𝐨𝐢𝐧𝐭𝟑 = 30.
(iii) Based on your sampling points, derive the probability 𝐩𝐫𝐨𝐛𝟒 that the total
impact is between 𝐩𝐨𝐢𝐧𝐭𝟒 = 50 and 𝐩𝐨𝐢𝐧𝐭𝟓 = 100.
(4) Assume that the median of the triangular distribution 𝐌𝐄𝐃𝐈𝐀𝐍_𝐭 derived in (1)-(iii)
is used as the AV in (Eq. 2), the mean of the data set 𝐌𝐄𝐀𝐍_𝐝 derived in (2) is used as
the ARO in (Eq. 1), and the probability 𝐩𝐫𝐨𝐛𝟑 derived in (3)-(ii) is used as the EF in (Eq.
2). Calculate the value of the ALE.

Use the following code
from dhCheck_Task1 import dhCheckCorrectness
def Task1(a, b, c, point1, point2, data, mu, sigma, xm, alpha,
num, point3, point4, point5):

 # TODO

return (prob1, prob2, MEAN_t, MEDIAN_t, MEAN_d, VARIANCE_d,
prob3, prob4, ALE)
