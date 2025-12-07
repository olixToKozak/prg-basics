def powers(x,n):
    if n==1:
        return x
    return x*powers(x^n-1)