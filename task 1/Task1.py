import sys
import math
import itertools

def delt(N):
    d=set()
    for i in range(2, int(N**0.5)+1):
        if N%i==0:
            d.add(i)
            d.add(N//i)
    delete = sorted(d)
    return delete


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    R, B = [int(count) for count in input().split()]
    if int(math.sqrt(B))**2 == B:
        height=int(math.sqrt(B))+2
        print (height, height)
        return
    if len(delt(B))==0 or B==2:
        W, H = sorted([3, B+2], reverse=True)
        print (W, H)
        return
    
    h_w = (R/2) - 2
    B_height, B_width = [pair for pair in itertools.combinations(delt(B), 2) if sum(pair)==h_w and math.prod(pair)==B][0]

    height = (B_height+2)
    width = (B_width+2)
    
    W, H = sorted([height, width], reverse=True)
    print (W, H)
    return


if __name__ == '__main__':
    main()
