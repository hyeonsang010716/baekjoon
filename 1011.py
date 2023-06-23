import sys
import math
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    start , end = map(int,input().split())
    distance = end - start
    sq = int(math.sqrt(distance))
    if(distance == math.pow(sq,2)) : print(2*sq - 1)
    else:
        if distance - math.pow(sq,2) <= sq : print(2*sq)
        else : print(2*sq + 1)