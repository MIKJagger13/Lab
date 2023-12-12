def baby_step_giant_step(g, h, q):
    # Визначаємо параметр m
    m = int(q**0.5) + 1
    
    # Ініціалізуємо словник для зберігання значень логарифмів
    log = dict()
    p = 1
    
    # Заповнюємо словник логарифмів для baby steps
    for j in range(m):
        log[p] = j
        p = (p * g) % q
        
    # Визначаємо обернений елемент для giant steps
    inv = pow(g, (m * (q - 2)) % (q - 1), q)
    
    # Ініціалізуємо змінну для порівняння
    c = h
    
    # Проводимо baby step - giant step алгоритм
    for i in range(m):
        if c in log:
            return (i * m + log[c]) % q
        else:
            c = (c * inv) % q

# Зчитуємо вхідні значення з консолі
g, h, q = [int(i) for i in input().split()]

# Виводимо результат виклику функції
print(baby_step_giant_step(g, h, q))
