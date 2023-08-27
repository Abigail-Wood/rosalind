# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
#   k individuals are homozygous dominant for a factor,
#   m are heterozygous, and
#   n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
# allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample data: k=2 m=2 n=2

# Consider simulating inheritance on a number of small test cases in order to check your solution.

k = 30
m = 25
n = 22

# Solution 1
total = k + m + n

p_k1 = k / total
p_m1 = m / total
p_n1 = n / total

p_k2 = p_k1 * (k - 1) / (total - 1)
p_m2 = p_m1 * (m - 1) / (total - 1)

p_km = p_k1 * m / (total - 1) + p_m1 * k / (total - 1)
p_kn = p_k1 * n / (total - 1) + p_n1 * k / (total - 1)
p_mn = p_m1 * n / (total - 1) + p_n1 * m / (total - 1)

dominant = p_k2 + 0.75 * p_m2 + p_km + p_kn + 0.5 * p_mn
print(dominant)


# Solution 2
def calc_prob_dominance():
    """ Probability of at least 1 dominant allele is 1 - P(homozygous recessive)."""
    N = k + m + n
    div = N * (N - 1)
    return 1 - (n * (m + n - 1) + m * (m - 1) / 4) / div
