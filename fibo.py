def fibo(n) : # <int>
    """Return the n first Fibonocci numbers in a list"""

    n = int(n)
    i = 1
    loop = 0
    L = [0, 1]

    if n < 1 :
        L = [None]
        return L

    elif n == 1 :
        L = [0]
        return L

    else :    
        while loop < n - 2 :
            res = L[i] + L[i-1]
            L.append(res)
            i += 1
            loop += 1
    return L # <list>

def isfibo(x) :
    """Return True if it's a Fibonacci number, False otherwise"""
    
    x = int(x)
    L = [0, 1]
    i = 1

    if x in L :
        return True

    else :
        while True:
            res = L[i] + L[i-1]
            L.append(res)
            if x in L:
                return True
            if L[i] > x:
                return False
            i+=1

if __name__ == "__main__" :
    print("The 10 first Fibonacci numbers : {}".format(fibo(10)))
    print("Is 13 a Fibonacci number ? : {}".format(isfibo(13)))
    print("Is 789 a Fibonacci number ? : {}".format(isfibo(789)))