#aula 16 operações com algebra linear

# Este arquivo pode ser executado como código, ou inserido gradualmente
# no prompt para fins de estudo

# Em Python, operações em álgebra linear são primariamente realizadas com as bibliotecas 
# numpy e scipy.
# O módulo numpy.linalg providencia métodos para além de operações básicas, 
# como a multiplicação de matrizes e vetores,
# a decomposição de matrizes, o cálculo de autovalores e de normas, 
#a solução de sistemas lineares, entre outras.

import numpy as np

# operações básicas com vetores
x = np.random.rand(3) # vetor aleatório com 3 elementos
y = np.random.rand(3)

x + y  # soma de vetores
x * y  # multiplicação elemento a elemento

np.vdot(x, y)  # produto escalar
np.linalg.norm(x)  # norma euclidiana do vetor
np.cross(x, y)  # produto vetorial
x / np.linalg.norm(x)  # vetor unitário

# operações básicas com matrizes
A = np.random.rand(3, 3) # matriz 3x3 aleatória
B = np.random.rand(3, 3)

A + B  # soma de matrizes
A - B  # subtração de matrizes
A * B  # multiplicação elemento a elemento
A @ B  # multiplicação de matrizes
A.T    # transposição de matriz

# decomposição matricial
qA, rA = np.linalg.qr(A)  # decomposição QR
uA, sA, vA_T = np.linalg.svd(A)  # decomposição SVD (em valores singulares)

# autovalores
avals, avecs = np.linalg.eig(A)  # autovalores e autovetores de A

# solução de sistemas lineares e inversão de matrizes

b = np.random.rand(3)  # vetor b aleatório
x_hat = np.linalg.solve(A, b)  # solução do sistema Ax = b
x_lstsq = np.linalg.lstsq(A, b, rcond=None)  # solução de mínimos quadrados
inv_A = np.linalg.inv(A)  # inversa da matriz A

# normas matriciais e outros números
fro_A = np.linalg.norm(A, ord='fro')  # norma de Frobenius
two_norm_A = np.linalg.norm(A, ord=2)  # norma espectral (2-norma)
cond_A = np.linalg.cond(A)  # número de condicionamento da matriz A
det_A = np.linalg.det(A)  # determinante da matriz A
tr_A = np.trace(A)  # traço da matriz A

# o módulo scipy.linalg provê funcionalidades adicionais para álgebra linear, 
# incluindo mais métodos de decomposição,
# operações com matrizes especiais e outras funções avançadas.

import scipy as sp

# algumas fatorações
p, l, u = sp.linalg.lu(A)  # decomposição LU
b_range = sp.linalg.orth(A)  # base ortonormal para o espaço coluna de A
b_null = sp.linalg.null_space(A)  # base ortonormal para o núcleo de A

# matrizes especiais
sp.linalg.hadamard(4)  # matriz de Hadamard 4x4
sp.linalg.toeplitz([1, 2, 3], [1, 4, 5])  # matriz de Toeplitz
sp.linalg.hilbert(3)  # matriz de Hilbert 3x3