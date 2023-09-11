degree = int(input("Enter Degree: "))
coefs = []
for i in range(degree + 1):
    coef = int(input("Enter coefficient " + str(i + 1) + ": "))
    coefs.append(coef)

def findPossibleRoots(coefs):
    
    p = []
    for i in range(abs(coefs[len(coefs) - 1])):
        if (coefs[len(coefs) - 1] % (i + 1) == 0):
            p.append(i + 1)
    q = []
    for i in range(abs(coefs[0])):
        if (coefs[0] % (i + 1) == 0):
            q.append(i + 1)
    
    roots = q + p
    for i in range(len(q)):
        for j in range(len(p)):
            if (p[j] / q[i] not in roots):
                roots.append(p[j] / q[i])
    
    return roots

print("Coefficients:")
print(coefs)
roots = findPossibleRoots(coefs)
print("Possible Roots:")
print(roots)

from syntheticDivision import synthDiv
print("Synthetic Division Steps:")
realRoots = []

for i in range(len(roots)):
    newcoefs = synthDiv(coefs, roots[i])
    if (newcoefs[-1] == 0):
        realRoots.append(roots[i])
        coefs = newcoefs

for i in range(len(roots)):
    newcoefs = synthDiv(coefs, -roots[i])
    if (newcoefs[-1] == 0):
        realRoots.append(-roots[i])
        coefs = newcoefs

print("Real Distinct Roots:")
print(realRoots)


if (len(realRoots) != degree and len(coefs) <= 3):
    print("Coefficients for Quadratic Formula:")
    print(coefs)
    
    a = coefs[0]
    b = coefs[1]
    c = coefs[2]
    
    from quadraticFormula import quadForm
    
    print("Quadratic Formula Roots:")
    quadroots = quadForm(a,b,c)
    print(quadroots)
else:
    quadroots = None
print("\n******************************************\n")
print("Final Roots:")
prOut = ""
for i in range(len(realRoots)):
    prOut += str(realRoots[i]) + ", "
if (quadroots):
    prOut += str(quadroots[0]) + ", " + str(quadroots[1])
print(prOut)