from random import random
import time


methods = [dict.fromkeys,frozenset,list]

for m in methods:

    base_num = 1000
    nums = [base_num*10**i for i in range(5)]

    needles = [random() for _ in range(1000)]


    for j in nums:
        haystack = m([random() for _ in range(j)])

        now = time.time()
        found = 1
        for i in needles:
            if i in haystack:
                found += 1



        last_time = time.time() - now

        print(last_time)

    print('-------------------')
