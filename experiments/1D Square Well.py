"""
Learning experiment based on a VPython tutorial.

This script explores an iterative approach to the 1D square well.
The main project uses a finite-difference Hamiltonian matrix eigenvalue method.
"""

Web
VPython
3.2
g1 = graph(title="1D Square Well", xtitle="x", ytitle="psi", width=500, height=250)
f1 = gcurve(color=color.blue)
g2 = graph(xtitle="n", ytitle="<E>", width=500, height=250)
f2 = gcurve(color=color.red)
m = 1
a = 1
hbar = 1

x = 0
dx = 0.01
E = 4.9

xp = [0]
psip = [0]
psip2 = [0]

while x < a:
    x = x + dx
    xp = xp + [x]
    psip = psip + [0.2]
    psip2 = psip2 + [0.2]

psip[-1] = 0
psip2[-1] = 0

for i in range(len(xp)):
    f1.plot(xp[i], psip[i])


def Ex(tpsi, tx):
    tdx = tx[1] - tx[0]
    Et = 0
    for i in range(1, len(tx) - 1):
        Et = Et + (-hbar ** 2 / (2 * m)) * tpsi[i] * (tpsi[i + 1] - 2 * tpsi[i] + tpsi[i - 1]) / tdx
    I = 0
    for i in range(len(tpsi)):
        I = I + tpsi[i] ** 2 * tdx
    return (Et / I)


N = 1000
n = 0

while n < N:
    rate(500)
    fdata = []
    E = Ex(psip, xp)
    for i in range(1, len(xp) - 1):
        psip2[i] = (psip[i + 1] + psip[i - 1]) / (2 - (2 * m * E * dx ** 2) / hbar ** 2)
    for i in range(len(psip)):
        psip[i] = psip2[i]
    for i in range(len(psip)):
        fdata = fdata + [[xp[i], psip[i]]]
    f1.data = fdata
    n = n + 1

print("<E> = ", Ex(psip, xp))



