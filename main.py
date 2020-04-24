''' yumm1e3o

<방정식의 근사해; 뉴턴의 방법>

1. 방정식 f(X)=0의 해를 추측한다. y=f(X)의 그래프를 통해 근삿값을 추정할 수 있다.
2. n번째 근사해 X_n으로부터 n+1번째 근사해 X_n+1를 다음 식을 이용하여 구할 수 있다.

X_n+1 = X_n - f(X_n)/f'(X_n) ... (단, f'(X) != 0)

'''

#얕은 복사에서 주의할 점 : 해당 값이 할당되는 것이 아닌, 같은 메모리 주소를 바라보는 것이다.
#list

#각 X_n 값을 2차원 배열에 지정하여 저장 -> 0~m번째 칸 까지 자리수 모두 비교
# -> 원하는 소수점 아래 자릿수까지 값이 모두 같으면''으로 조건 변경

import fractions as fr
import math

def fx(f, x):
    ans, pw = fr.Fraction(0), fr.Fraction(1)
    for a in f:
        ans += a * pw
        pw *= x
    return ans

def getfront(frac, d):
    return int((frac - frac // 1) * 10 ** d // 1)

if __name__ == "__main__":
    n = int(input("n차 다항식? ",))
    f = []
    for i in range(n + 1): f.append(fr.Fraction(input("x^%d의 계수 = "%i)))
    df = f[1:]
    for i in range(n): df[i] *= i + 1

    lx, nx = fr.Fraction(input("초항 = ")), 0
    d = int(input("소수점 아래 몇번째 자리까지? "))
    while True:
        nx = lx - fx(f, lx) / fx(df, lx)
        if getfront(lx, d) == getfront(nx, d): break
        lx = nx
    
    print("%d.%0*d"%(int(lx // 1), d, getfront(lx, d)))