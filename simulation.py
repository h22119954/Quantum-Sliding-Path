# Qiskitと基本ライブラリ
from qiskit import QuantumCircuit, Aer
from qiskit.quantum_info import DensityMatrix
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# パラメータ
N = 2
T_total = 10
delta_t = 1
kappa0 = 0.05
E, M, A = 0.8, 0.3, 0.7
n = 5
weights = [1.0]*n
S = 0.5
r, r0 = 2.0, 1.0
alpha = 2.0

# --------------------------
# 弱測定強度
def base_kappa():
    return kappa0 * (1 + 0.5*E) * (1 + 0.2*M) * (1 + 0.8*A)

def kappa_effective():
    kappa_total = sum([w * base_kappa() for w in weights])
    return kappa_total * np.exp(-alpha*S) / (1 + (r/r0)**2)

# --------------------------
# 初期状態
qc = QuantumCircuit(N)
for q in range(N):
    qc.h(q)
rho = DensityMatrix(qc)
coherence_list = []

# --------------------------
# 弱測定関数
def apply_weak_measurement(rho, kappa_val):
    p = kappa_val
    new_rho = (1-p)*rho.data + p * np.dot(np.array([[1,0],[0,-1]]), rho.data) @ np.array([[1,0],[0,-1]])
    return DensityMatrix(new_rho)

# --------------------------
# シミュレーション
for t in range(T_total):
    for q in range(N):
        qc.rx(np.pi/20, q)
    rho = DensityMatrix(qc)
    rho = apply_weak_measurement(rho, kappa_effective())
    gamma = np.trace(rho.data @ rho.data).real
    coherence_list.append(gamma)

# --------------------------
# 結果表示
plt.plot(range(T_total), coherence_list, marker='o')
plt.xlabel('Time step t')
plt.ylabel('Coherence Γ(t)')
plt.title('Coherence with Collective Consciousness + Shield + Distance')
plt.grid(True)
plt.show()
