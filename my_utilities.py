#utils
def isprime(v):
    return (len([i for i in range(1, v+1) if v % i == 0]) == 2)
def get_factors(v):
    return [i for i in range(1, v+1) if v % i == 0]
def gcf(a, b):
    return [i for i in range(1, a + b) if a % i== 0 and b % i == 0][-1]
def lcm(a, b):
    return (a * b) / gcf(a, b)
def floor(a):
    return int(a // 1)
def factorial(a):
    if a < 2:
        return 1
    else:
        return a * factorial(a-1)
def sign(a):
    if a == 0:
        return 0
    else:
        return abs(a) / a
def combinations(n, p):
    return factorial(n) / (factorial(n-p) * factorial(p))
def permutations(n, p):
    return factorial(n) / factorial(n-p)
def quadratic_coeff(val): #takes string of quadratic -> list of coefficients.
  #assumes ax^2 + bx + c, but can take any number of spaces or value lengths.
  #prune spaces, alloc negatives for proper interpretation when
  #values are split at + terms
  val = val.replace(' ', ''); val = val.replace('-', '+-')
  val = val.split('+')
  #remove invalid terms ''
  val = [i for i in val if i]
  nval = []
  if len(val) != 3:
      raise ValueError('Term(s) required for quadratic interpretation were missing.')
      return []
  for i in val:
    #get rid of x terms and all after them (for x^2 term)
    i = i.split('x')[0]
    #Special cases: -1, 1
    if i == '-':
      i = -1
    elif not i:
      i = 1
      #convert to int, finally
    nval.append(int(i))
  #COEFF LIST: [a, b, c]
  return nval
#MISC PYTHON THINGS:
def rm_duplicates(a):
    return [i for n, i in enumerate(a) if i not in a[:n]]
def cumulative(L, f, total = 0):
    n = total
    for i in L:
        n = f(i, n)
    return n
def _sum_example(L):
    x = lambda a, b: a + b
    return cumulative(L, x)
#STATS:
def mean(a):
    return sum(a) / len(a)
def median(a):
    x = len(a)
    if x % 2 == 1: #A B C D E
        return a[x//2]
    else: #A B C D E F
        return mean(a[x//2 - 1], a[x//2]) 

def mode(a):
    var_table = rm_duplicates(a)
    var_count = []
    for i in var_table:
        var_count.append(a.count(i))
    return var_count.sort()[-1]
def deviation(val, a):
    return (val - mean(a)) ** 2
def variance(a):
    return mean(list(map(deviation, a)))
def stddev(a):
    return sqrt(variance(a))

#SQRT
def _sqrt_babylon(a, xN = 1, iter_max = 25, e_max = 1e-7, iter_num = 0):
    epsilon = abs((a - xN ** 2) / (2 * xN))
    if iter_num > iter_max or epsilon < e_max:
        return xN
    else:
        return _sqrt_babylon(a, ((a/xN) + xN)/2, iter_max, e_max, iter_num + 1)
def _f_sqrt_approx(a, base = 2): #gives very ballpark estimate for square root, so that sqrt is faster
    approx_log = 0
    v = 2
    while v < a:
        approx_log += 1
        v = v * base
    if approx_log % 2 != 0 and base < a:
        return _f_sqrt_approx(a, base + 1)
    return base ** (approx_log // 2)
def sqrt(a, margin = 1e-16, iterlim = 100):
    ballpark = _f_sqrt_approx(a)
    return _sqrt_babylon(a, ballpark, iterlim, margin)