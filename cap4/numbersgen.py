#File: numbersgen.py
"""Definisci alcuni generatori di successioni numeriche."""

def fibonacci(n):
    """Genera numeri di fibonacci."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def wondrous(n):
    """Genera numeri HOTPO (Half Or Triple Plus One)."""
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    else:
        yield 1
