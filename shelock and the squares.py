import math as r
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):
    a1 = r.sqrt(a);
    b1 = r.sqrt(b);
    a2 = r.ceil(a1);
    b2 = r.floor(b1);
    a = []
    for i in range(a2, b2 + 1):
        a.append(i * i)
    return len(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
