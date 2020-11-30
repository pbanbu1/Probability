import sys
import random
from collections import Counter
# from scipy.stats import uniform  

i = 0
r_arr = []
while i < 1000:
    rv = random.uniform(0, 1)
    r_arr.append(10**rv)
    i += 1
start_digits = [str(x)[2] for x in r_arr]
print(start_digits)

# c = Counter(start_digits)
# for letter in '123456789':
#     print  ((c[letter])/1000)

