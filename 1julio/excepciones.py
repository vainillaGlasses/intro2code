dividendo = 5
divisor = 0

try:
    cociente = dividendo / divisor
except IOError:
    print("ERROR en entradas y salidas")
except ZeroDivisionError:
    cociente = dividendo / 10
else:
    print("no divido por cero")