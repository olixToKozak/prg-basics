def f(n):
    a=0
    b=1
    fiba=0
    fibb=0
    for i in range(n-1):
        fibb = a+b
        fiba = b
        a = fiba
        b = fibb
    return a
        
        
        
#   0 1 1 2 3 5 8 13
#   a+b=1 
#     a+b=2
#       a+b=3