def newton_raphson(equation, x0, epsilon, max_iter):
    # Convertir la ecuación a funciones
    f = lambda x: eval(equation)
    f_prime = lambda x: (eval(equation.replace('x', f'({x} + 1e-8)')) - f(x)) / 1e-8

    # Inicializar el contador de iteraciones
    iter_count = 0

    # Repetir mientras la diferencia sea mayor que el umbral y no se supere el máximo de iteraciones
    while True:
        # Aplicar la fórmula de Newton Raphson
        x1 = x0 - f(x0) / f_prime(x0)

        # Actualizar la estimación y la diferencia
        x0, diff = x1, abs(x1 - x0)

        # Incrementar el contador de iteraciones
        iter_count += 1

        # Imprime la iteración actual
        print(f"Iteración {iter_count}: Estimación = {x0:.5f}, Diferencia = {diff:.5f}")

        # Verifica las condiciones de salida
        if diff <= epsilon or iter_count >= max_iter:
            break

    # Devuelve la estimación final y el número de iteraciones
    return x0, iter_count

# ingresa la ecuación
equation = input("Ingrese la ecuación en términos de 'x': ")

# Elige la estimación inicial, y el máximo de iteraciones
x0 = float(input("Ingrese la estimación inicial (x0): "))
epsilon = 0.00001
max_iter = int(input("Ingrese el máximo de iteraciones: "))

# Llama a la función de Newton Raphson
root, iter_count = newton_raphson(equation, x0, epsilon, max_iter)

# Imprime el resultado final
print(f"\nLa raíz es {root:.5f}, encontrada en {iter_count} iteraciones.")
