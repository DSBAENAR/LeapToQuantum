import math
def ComplexSum(c1,c2):
    Re=c1[0]+c2[0]
    Im=c1[1]+c2[1]
    Resultado=print("{}{}i".format(Re,Im))
    if Im>0:
        Resultado=print("{} + {}i".format(Re,Im))
    elif Im<0:
        Resultado=print("{}{}i".format(Re,Im))
    else:
        Resultado=print("{}".format(Re,Im))
    return Resultado
def ComplexSub(c1,c2):
    Re=c1[0]-c2[0]
    Im=c1[1]-c2[1]
    Resultado=print("{}{}i".format(Re,Im))
    if Im>0:
        Resultado=print("{} + {}i".format(Re,Im))
    elif Im<0:
        Resultado=print("{}{}i".format(Re,Im))
    else:
        Resultado=print("{}".format(Re,Im))
    return Resultado
def ComplexDiv(c1,c2):
    Re=((c1[0]*c2[0])+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2)
    Im=((c2[0]*c1[1])-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2)
    if Im>0:
        Resultado=print("{} + {}i".format(Re,Im))
    elif Im<0:
        Resultado=print("{}{}i".format(Re,Im))
    else:
        Resultado=print("{}".format(Re,Im))
    return Resultado
def ComplexMult(c1,c2):
    Re=(c1[0]*c2[0])-(c1[1]*c2[1])
    Im=(c2[0]*c1[1])+(c1[0]*c2[1])
    if Im>0:
        Resultado=print("{} + {}i".format(Re,Im))
    elif Im<0:
        Resultado=print("{}{}i".format(Re,Im))
    else:
        Resultado=print("{}".format(Re,Im))
    return Resultado
def ComplexMod(c1):
    Resultado=(c1[0]**2+c1[1]**2)**0.5
    return Resultado
def ComplexConjugate(c1):
    Re=c1[0]
    Im=-c1[1]
    if Im>0:
        Resultado=print("{} + {}i".format(Re,Im))
    elif Im<0:
        Resultado=print("{}{}i".format(Re,Im))
    else:
        Resultado=print("{}".format(Re,Im))
    return Resultado
def CartesianToPolar(c1):
    try:
        rho=ComplexMod(c1)
        tetha=math.atan(c1[1]/c1[0])
        if tetha>2*math.pi:
            tetha=tetha-2*math.pi
            Resultado=print("({},{})".format(rho,tetha))
        elif tetha<0:
            tetha=tetha+2*math.pi
            Resultado=print("({},{})".format(rho,tetha))
        else:
            Resultado=print("({},{})".format(rho,tetha))
        return Resultado
    except:
        if c1[0]==0 and c1[1]>0:
            Resultado=print("({},{})".format(rho,"pi/2"))
        elif c1[0]==0 and c1[1]<0: 
            Resultado=print("({},{})".format(rho,"3pi/2"))
        return Resultado
def PolarToCartesian(c1):
   
    Re=c1[0]*math.cos(c1[1])
    Im=c1[0]*math.sin(c1[1])
    Resultado=print("({},{})".format(Re,Im))
    return Resultado

def ComplexPhase(c1):
    try:
        phase=math.atan(c1[1]/c1[0])
        if phase>2*math.pi:
            phase=phase-2*math.pi
            Resultado=print("La fase del número complejo es: {}".format(phase))
        elif phase<0:
            phase=phase+2*math.pi
            Resultado=print("La fase del número complejo es: {}".format(phase))
        return Resultado
    except:
        c1[0]==0 and c1[1]>0
        if c1[0]==0 and c1[1]>0:
            Resultado=print("La fase del número complejo es: {}".format("pi/2"))
        elif c1[0]==0 and c1[1]<0: 
            Resultado=print("La fase del número complejo es: {}".format("3pi/2"))
        return Resultado
ComplexPhase([0,-1])



