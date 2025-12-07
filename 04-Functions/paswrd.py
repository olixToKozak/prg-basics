def f(password):
    if len(password) >= 6:
        for i in password:
            if str(password).count(i) > 1:
                return False
        else:
            return True
    else:
        return False