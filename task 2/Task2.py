import sys
import itertools 

def main():
    nums = [int(input().strip()) for i in range (10)]
    
    res=set()
    difference = 100

    for k in range (1, 11):
        for arr in itertools.combinations(nums, k):
            sm = sum(arr)
            dif = abs(100-sm)
            if dif <= difference:
                res.add(sm)
                difference = dif
    res = sorted(res, key=lambda x: (abs(100-x), -x))
    print(res[0])
    return


if __name__ == '__main__':
    main()
