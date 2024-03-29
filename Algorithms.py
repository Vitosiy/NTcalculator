import math
import functools
from functools import reduce
import re
from typing import Dict


# Проверочки на простоту
##############################################################################
def is_prime(n):
    if n < 0: n = -n
    if n < 2: return False
    if (n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)): return True
    return isprimeE(n, 2) and isprimeE(n, 3) and isprimeE(n, 5)


def isprimeF(n, b):
    return (pow(b, n - 1, n) == 1)


def isprimeE(n, b):
    if (not isprimeF(n, b)): return False
    r = n - 1
    while (r % 2 == 0): r //= 2
    c = pow(b, r, n)
    if (c == 1): return True
    while (1):
        if (c == 1): return False
        if (c == n - 1): return True
        c = pow(c, 2, n)


# Алгоритмы Евклида
##############################################################################
def gcd(a, b):  # прямой
    if a < b:
        tmp = a
        a = b
        b = tmp
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b, flag:bool = 0):  # расширенный
    if a > b:
        tmp = a
        a = b
        b = tmp
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    if flag == 0:
        return b, x, y
    else:
        return x


def egcd_origin(a, b):
    gcd, x, y = egcd(a, b)
    return "НОД(A, B): {0}, x = {1}, y = {2}".format(gcd, x, y)


##############################################################################

# Сравнение первой степени
##############################################################################
def compare(a, b, mod):
    if mod == 0:
        return "Модуль должен быть натуральным числом!"
    d = gcd(a, mod)
    a = a % mod
    b = b % mod
    if (d > 1) and (b % d != 0):
        return "Нет решений"
    elif d == 1:
        c = egcd(a, mod, 1)
        b = b * c
        b = b % mod
        return "x сравним с {0} по модулю {1}".format(b, mod)
    elif (d > 1) and (b % d == 0):
        tmp_mod = mod
        a, b, mod = a // d, b // d, mod // d
        c = egcd(a, mod, 1)
        b = b * c
        b = b % mod
        res: str = str(b)

        for i in range(1, d):
            res += ", " + str(b + mod * i)
        return "x сравним с {0} по модулю {1}".format(res, tmp_mod)
    else:
        return "Ошибка! Нет решений!"

##############################################################################


# Китайская теорема об остатках: x == b(mod)
#  mod = [2, 3, 5, 7]
#  b   = [1, 2, 2, 5]
##############################################################################
def chinese_remainder(b, mods):
    for i in range(len(mods)):
        for j in range(len(mods)):
            if i == j: continue
            if not gcd(mods[i], mods[j]) == 1:
                return "Модули не взаимно простые! Система не разрешима!"
    sum = 0
    M = reduce(lambda b, a: b * a, mods)
    for mod_i, b_i in zip(mods, b):
        M_i = M // mod_i
        sum += b_i * mul_inv(M_i, mod_i) * M_i
    return f"x сравним с {sum % M} по модулю {M}"

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

##############################################################################


# Cравнение по модулю степени простого числа
##############################################################################
def diff(data):  # нахождение производной
    data_diff = {}
    for index in data:
        if index == 0:
            continue
        data_diff[index - 1] = data[index] * index
    return data_diff


def read(string) -> Dict[int, int]:  # сборка словаря из строки
    new_string = ''
    for symbol in string:
        if symbol == " ":
            continue
        new_string += symbol
    for symbol in new_string:
        if not symbol == 'x' and not symbol.isdigit() and not symbol == '^' and not symbol == '-' and not symbol == '+':
            return -1
    parts = re.findall(r'(-?\d*x?\^?-?\d*)', new_string)
    parts = [part.strip() for part in parts]
    data = {}
    for part in parts:
        minus = 0
        if part == "":
            continue
        for symbol in part:
            if not symbol == 'x' and not symbol.isdigit() and not symbol == '^' and not symbol == '-':
                return -1
        coefficient = re.search(r'^(-?\d+)', part)
        degree = re.search(r'x\^(\d+)', part)
        if part.startswith("-"):
            minus = 1
        if coefficient is None:
            coefficient = 1
        else:
            coefficient = int(coefficient.group(1))
        if not degree:
            if 'x' in part:
                degree = 1
            else:
                degree = 0
        else:
            degree = int(degree.group(1))
        data[degree] = coefficient
    return data


def mod(data, module):  # взятие словаря по модулю
    data_diff = {}
    for index in data:
        data_diff[index] = data[index] % module
    return data_diff


def solution(data, x):  # подставление найденного x в уравнение
    data_sol = 0
    for index in data:
        data_sol += data[index] * x ** index
    return data_sol


def compare_n(string: str, module: int, deg: int):
    m = module
    if not is_prime(m):
        return -2
    data = read(string)
    if data == -1:
        return -1
    data_diff = diff(data)
    a, b, t = 0, 0, 0
    solution_t = 0
    fx = mod(data, module)
    for deg_iter in range(1, deg + 1):
        if deg_iter == 1:
            for i in range(module):
                solution_x = 0
                for tmp in fx:                          #подставляем значения в выражение по модулю
                    solution_x += fx[tmp] * i ** tmp    #сумма = коэффициент при x * подставленный x в степени по массиву
                solution_x = solution_x % module
                if solution_x == 0:
                    x0 = i
                    a = i
                    b = module ** deg_iter
        else:
            for i in range(module):
                solution_x = 0
                solution_x = solution_fx + solution_fx_diff * i
                solution_x = solution_x % module
                if solution_x == 0:
                    t = i
                    solution_t = a + b * t
                    a = solution_t
                    b = module ** deg_iter
        solution_fx = (solution(data, a) / module ** deg_iter) % module
        solution_fx_diff = solution(data_diff, a) % module
    return f"{string} сравнимо с {solution_t} по модулю {module ** deg}"

##############################################################################


# Символ Лежандра
############################################################################## 
def isPrime_leg(a):
    return all(a % i for i in range(2, a))


def factorize_leg(n):
    factors = []

    p = 2
    while True:
        while n % p == 0 and n > 0:
            factors.append(p)
            n = n // p
        p += 1
        if p > n // p:
            break
    if n > 1:
        factors.append(n)
    return factors


def calculateLegendre(a, p):
    if a >= p or a < 0:                                 #Свойство 2
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:                              #Свойство 3
        return a
    elif a == 2:                                        #Свойство 5
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:                                    #Свойство 4
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not isPrime_leg(a):                            #Свойство 1
        factors = factorize_leg(a)
        product = 1
        for pi in factors:
            product *= calculateLegendre(pi, p)
        return product
    else:
        if ((p - 1) // 2) % 2 == 0 or ((a - 1) // 2) % 2 == 0:  #Свойство 6
            return calculateLegendre(p, a)
        else:
            return (-1) * calculateLegendre(p, a)


##############################################################################


# Метод Шенкса
###############################################################################

def RESSOL(n, p):
    if not calculateLegendre(n, p) == 1:
        return "Введён не квадратичный вычет по модулю"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return f"Корни: {r}, {p-r}"
    z = 2
    for z in range(2, p):
        if calculateLegendre(z, p) == -1:
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return f"Корни: {r}, {p-r}"

##############################################################################


# Первообразный корень по модулю
##############################################################################
def factorone(n):
    if (is_prime(n)): return n
    for fact in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % fact == 0: return fact
    return factorPR(n)


def factorPR(n):
    numsteps = 2 * math.floor(math.sqrt(math.sqrt(n)))
    for additive in range(1, 5):
        fast = slow = 1;
        i = 1
        while i < numsteps:
            slow = (slow * slow + additive) % n
            i = i + 1
            fast = (fast * fast + additive) % n
            fast = (fast * fast + additive) % n
            g = gcd(fast - slow, n)
            if (g != 1):
                if (g == n):
                    break
                else:
                    return g
    return 1


def factor(n):
    if ((abs(n) == 1) or (n == 0)): return -1
    factspow = []
    currfact = None
    thecount = 1
    for thefact in factors(n):
        if thefact != currfact:
            if currfact != None:
                factspow += [(currfact, thecount)]
            currfact = thefact
            thecount = 1
        else:
            thecount += 1
    factspow += [(thefact, thecount)]
    return tuple(factspow)


def factors(n):
    if n < 0: n = -n
    if (is_prime(n)):
        return [n]
    fact = factorone(n)
    if ((abs(n) == 1) or (n == 0)): return -1
    facts = factors(n // fact) + factors(fact)
    facts.sort()
    return facts


def euler_phi(n):
    if n == 1: return 1
    if n <= 0: return 0

    return functools.reduce(lambda a, x: a * (x[0] ** (x[1] - 1)) * (x[0] - 1), factor(n), 1)


def prime_divisors(n):
    res = factors(n)
    if res == -1:
        return -1
    else:
        return tuple(set(res))


def carmichael_lambda(n):
    if n == 1: return 1
    if n <= 0: return -2


    def _carmichael_lambda_primepow(theprime, thepow):
        if ((theprime == 2) and (thepow >= 3)):
            return (2 ** (thepow - 2))
        else:
            return (theprime - 1) * (theprime ** (thepow - 1))

    return functools.reduce(lambda accum, x: (accum * x) // gcd(accum, x),
                            tuple(_carmichael_lambda_primepow(*primepow) for primepow in factor(n)), 1)


def is_primitive_root(g, n):
    if gcd(g, n) != 1: return False
    order = euler_phi(n)
    if carmichael_lambda(n) != order: return False
    orderfacts = prime_divisors(order)
    if orderfacts == -1:
        return -1
    for fact in orderfacts:
        if pow(g, order // fact, n) == 1: return False
    return True
##############################################################################
