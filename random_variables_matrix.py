import numpy as np

# cov(a'*X,X'*b) = a'*V(X)*b
V = np.array([[4, -1, 0], [-1, 3, -1], [0, -1, 2]])

# a)
# V(A*X) = A*V(X)*A^T

A = np.array([1, 1, 1])

# Находим дисперсию случайной величины D(X1+X2+X3)
V_1 = A @ V @ A.T

print("a) Дисперсия D(X1+X2+X3):", V_1)

# b)
A = np.array([1, 0, -1])

V_2 = A @ V @ A.T

print("b) Дисперсия D(X1 - X3):", V_2)

# c)
A = np.array([1, 1, -1])

V_3 = A @ V @ A.T

print("c) Дисперсия D(X1+X2-X3):", V_3)

# d)
A = np.array([4, 3, 2])

V_4 = A @ V @ A.T

print("d) Дисперсия D(4*X1+3*X2+2*X3):", V_4)

# e)
A = np.array([1, 0, 3])

V_5 = A @ V @ A.T

print("e) Дисперсия D(X1+3*X3):", V_5)

# f)
A = np.array([1, -1, -2])

V_6 = A @ V @ A.T

print("f) Дисперсия D(X1-X2-2*X3):", V_6)


####################################
# cov(a'*X,X'*b) = a'*V(X)*b
# g)
a_t = np.array([1, 1, 0])
b = np.array([0, 1, 1]).T
cov_ab = a_t @ V @ b

print("g) Ковариация cov(a'*X,X'*b):", cov_ab)

# h)
a_t = np.array([1, 1, 0])
b = np.array([-1, 1, 0]).T
cov_ab = a_t @ V @ b

print("h) Ковариация cov(a'*X,X'*b):", cov_ab)

# i)
a_t = np.array([1, 1, 0])
b = np.array([0, 1, -1]).T
cov_ab = a_t @ V @ b

print("i) Ковариация cov(a'*X,X'*b):", cov_ab)


#######################
# Крокодил Утундрий - риск менеджмент
print("Вариант 1 - Крокодил Утундрий")
# R = w1*r(X1) + w2*r(X2) + w3*r(X3) - доходность портфеля
# E[R] = w1*E[X1] + w2*E[X2] + w3*E[X3] - ожидаемая доходность портфеля
# sqr(D) - риск портфеля

# a) найдите математическое ожидание доходности портфеля
# expectation of return
# E[R1] = 15, E[R2] = 20, E[R3] = 25
ER = np.array([15, 20, 25]).T

# b) составьте ковариационную матрицу доходностей активов

VR = np.array([[50, 10, 20], [10, 100, -30], [20, -30, 150]])

# c) найдите ожидаемые доходности портфелей A и B

wA = np.array([1 / 2, 1 / 2, 0]).T
wB = np.array([1 / 3, 1 / 3, 1 / 3]).T

EA = wA.T @ ER

EB = wB.T @ ER

print("c) Ожидаемая доходность портфеля A:", EA)
print("c) Ожидаемая доходность портфеля B:", EB)

# d) найдити риск портфеля A и B
stdA = np.sqrt(wA.T @ VR @ wA)
stdB = np.sqrt(wB.T @ VR @ wB)

print("d) Риск портфеля A:", stdA)
print("d) Риск портфеля B:", stdB)

# e) какой из портфеоей имеет большую ожидаемую доходность, а какой больший риск

print("expectation retunrns for A: ", EA)
print("expectation retunrns for B: ", EB)
print("risk for A: ", stdA)
print("risk for B: ", stdB)

# f) найдите коэффициент ковариации между доходностями портфелей A и B

#  cov(a'X, X'b) = a'*V(X)*b
cov_AB = wA.T @ VR @ wB

print("f) Коэффициент ковариации между доходностями портфелей A и B:", cov_AB)

# g) найдите коэффициент корреляции между доходностями портфелей A и B

corr_AB = cov_AB / (stdA * stdB)

print("g) Коэффициент корреляции между доходностями портфелей A и B:", corr_AB)

####################### Вариант 2
print("Вариант 2 - Крокодил Утундрий")
# R = w1*r(X1) + w2*r(X2) + w3*r(X3) - доходность портфеля
# E[R] = w1*E[X1] + w2*E[X2] + w3*E[X3] - ожидаемая доходность портфеля
# sqr(D) - риск портфеля

# a) найдите математическое ожидание доходности портфеля
# expectation of return
# E[R1] = 15, E[R2] = 20, E[R3] = 25
ER = np.array([5, 10, 15]).T

# b) составьте ковариационную матрицу доходностей активов

VR = np.array([[50, 10, -10], [20, 100, 10], [-10, 10, 150]])

# c) найдите ожидаемые доходности портфелей A и B

wA = np.array([1 / 2, 1 / 2, 0]).T
wB = np.array([0, 1 / 2, 1 / 2]).T

EA = wA.T @ ER

EB = wB.T @ ER

print("c) Ожидаемая доходность портфеля A:", EA)
print("c) Ожидаемая доходность портфеля B:", EB)

# d) найдити риск портфеля A и B
stdA = np.sqrt(wA.T @ VR @ wA)
stdB = np.sqrt(wB.T @ VR @ wB)

print("d) Риск портфеля A:", stdA)
print("d) Риск портфеля B:", stdB)

# e) какой из портфеоей имеет большую ожидаемую доходность, а какой больший риск

print("expectation retunrns for A: ", EA)
print("expectation retunrns for B: ", EB)
print("risk for A: ", stdA)
print("risk for B: ", stdB)

# f) найдите коэффициент ковариации между доходностями портфелей A и B

#  cov(a'X, X'b) = a'*V(X)*b
cov_AB = wA.T @ VR @ wB

print("f) Коэффициент ковариации между доходностями портфелей A и B:", cov_AB)

# g) найдите коэффициент корреляции между доходностями портфелей A и B

corr_AB = cov_AB / (stdA * stdB)

print("g) Коэффициент корреляции между доходностями портфелей A и B:", corr_AB)


# значения для случайных заданий
ER = np.array([5, 10, 15]).T
VR = np.array([[50, 10, -10], [20, 100, 10], [-10, 10, 150]])
wA = np.array([1 / 2, 1 / 2, 0]).T
wB = np.array([0, 1 / 2, 1 / 2]).T


# task 16
def get_E_and_D_of_port(ER, VR, w):
    Eport = w.T @ ER
    Dport = w.T @ VR @ w
    return [Eport, Dport]


print("E and D of port A: ", get_E_and_D_of_port(ER, VR, wA))

# task 17
w17 = np.array([0.2, 0.3, 0.5]).T
print("E and D of port 17: ", get_E_and_D_of_port(ER, VR, w17))


# task 18
def calc_2_port(ER, VR, wA, wB):
    EA = wA.T @ ER
    EB = wB.T @ ER
    stdA = np.sqrt(wA.T @ VR @ wA)
    stdB = np.sqrt(wB.T @ VR @ wB)
    cov_AB = wA.T @ VR @ wB
    corr_AB = cov_AB / (stdA * stdB)
    return [EA, EB, stdA, stdB, cov_AB, corr_AB]
