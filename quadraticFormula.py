def quadForm(a, b, c):
    import math
    t1 = -b
    t2 = (b**2) - (4 * a * c)
    if (t2 >= 0):
        t2 = math.sqrt(t2)
        return [(t1+t2) / (2 * a), (t1 - t2) / (2 * a)]
    else:
        out = 0
        t2 = abs(t2)
        for i in range(int(t2), 0, -1):
            if (t2 % (i**2) == 0):
                out = i
                t2 = t2 / (i ** 2)
                break
        t1 /= (2 * a)
        out /= (2 * a)
        if (out == 0):
            out = ''
        if (t1 == 0):
            return [str(out) + "i*sqrt(" + str(t2) + ")", "-" + str(out) + "i*sqrt(" + str(t2) + ")"]
        
        return [str(t1) + " + " + str(out) + "i*sqrt(" + str(t2) + ")", str(t1) + " - " + str(out) + "i*sqrt(" + str(t2) + ")"]