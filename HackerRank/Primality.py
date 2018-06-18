import math
def prime_check(num, primes):
    if num == 1:
        return False
    if num == 2:
        return True
    else:
        if int(num/2)+1 > primes[-1]:
            for item in range(primes[-1], int(math.sqrt(num))+1, 2):
                if prime_check(item, primes):
                    primes.append(item)
        for item in primes:
            if num == item:
                return True
            elif num%item == 0:
                return False
        return True

def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    it = int(input())
    for i in range(it):
        if prime_check(int(input()), primes):
            print('Prime')
        else:
            print('Not prime')

if __name__ =='__main__':
    main()