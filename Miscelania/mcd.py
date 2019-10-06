def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)
distancias=[1246,2254,1008]

##num1 = int(input("Introduce el primer numero: "))
##num2 = int(input("Introduce el segundo numero: "))

print("MDC ", distancias[0]," y ", distancias[2]," = ", mcd(distancias[0], distancias[2]))
