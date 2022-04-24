import math

E = 0.00001

def dydx(x, y):
    return math.sin(x) # исходная функция -cos(x)

def rungeKutta4x(x0, y0, x, h):
    funcVal = []
    x0Copy = x0

    for i in range(2):
        x0 = x0Copy
        n = (int)((x - x0)/h) 
        y = y0
        for j in range(n):
            k1 = h * dydx(x0, y)
            k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * dydx(x0 + h, y + k3)

            y += (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

            x0 += h
        funcVal.append(y)
        h /= 2

    x0 = x0Copy
    n = (int)((x - x0)/h) 
    y = y0

    i = 0
    while abs(funcVal[i] - funcVal[i + 1]) > E * 15:
        for j in range(1, n + 1):
            k1 = h * dydx(x0, y)
            k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * dydx(x0 + h, y + k3)

            y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

            x0 = x0 + h
        funcVal.append(y)
        h /= 2
    return funcVal

x0 = 0
y0 = -1
x = 1
h = 0.1

funcVal = rungeKutta4x(x0, y0, x, h)

for i in range(len(funcVal)):
    print('Y({0}) = {1}'.format(x, funcVal[i]))
