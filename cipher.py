def modular_inverse(a, m):
    x,y, u,v = 0,1, 1,0
    b = m
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    fpb = b
    if (fpb != 1): return None
    else: return x % m

def encrypt(password, kunci):
    ans = ""
    for t in password:
        if ('a' <= t <= 'z'):
            ans += chr((( kunci[0]*(ord(t) - ord('a')) + kunci[1] ) % 26) + ord('a'))
        elif ('A' <= t <= 'Z'):
            ans += chr((( kunci[0]*(ord(t) - ord('A')) + kunci[1] ) % 26) + ord('A'))
        else:
            ans += t
    return ans
    #return ''.join([ chr((( kunci[0]*(ord(t) - ord('a')) + kunci[1] ) % 26) + ord('a')) for t in password.lower().replace(' ', '') ])

def decrypt(cipher, kunci):
    ans = ""
    for c in cipher:
        if ('a' <= c <= 'z'):
            ans += chr((( modular_inverse(kunci[0], 26)*(ord(c) - ord('a') - kunci[1])) % 26) + ord('a'))
        elif ('A' <= c <= 'Z'):
            ans += chr((( modular_inverse(kunci[0], 26)*(ord(c) - ord('A') - kunci[1])) % 26) + ord('A'))
        else:
            ans += c
    return ans

#a = "AdMiN"
#kunci = [7, 1]
#b = encrypt(a, kunci)
#c = decrypt(b, kunci)
#print(a,b,c)


    