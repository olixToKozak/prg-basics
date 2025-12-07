def f(n):
    ast = ''
    if n<=1:
        return n*'*'
    else:
        for i in range(n):
            if i < n-1:
                ast = ast + '*/'
            else:
                ast = ast + '*'
        return ast
    
