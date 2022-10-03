def bin_umnoz(a, b):
    na, nb = len(a), len(b)
    res = [False] * (na+nb)
    b = [True if d == '1' else False for d in b[::-1]]
    a = [True if d == '1' else False for d in a[::-1]]
    
    for i in range(nb):
        if b[i]:
            t = False
            for j in range(na):
                res[i+j], t = res[i+j]^a[j]^t, (res[i+j]+a[j]+t) > 1
            res[i+j+1] = t 
    tmp = ['1' if d else '0' for d in res[::-1]]
    return ''.join(tmp).lstrip('0')
 
 
num1 = input()
num2 = input()
res_ab = int(num1,2)*int(num2,2)
ab_umnoz = bin_umnoz(num1, num2)
print(ab_umnoz)
