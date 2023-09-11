def synthDiv(coefs, root):
    outputCoefs = [coefs[0]]
    for i in range(len(coefs) - 1):
        holdAdd = outputCoefs[i] * root
        outputCoefs.append(coefs[i + 1] + holdAdd)
    print(outputCoefs)
    return outputCoefs