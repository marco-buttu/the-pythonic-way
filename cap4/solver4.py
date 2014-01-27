def solver(eq: str, var='x'):
    """Restituisci la soluzione di una equazione lineare di primo grado in una incognita.

    La funzione solver() prende come primo argomento una stringa rappresentativa di una
    equazione di primo grado in una incognita e restituisce la soluzione dell'equazione: 

        >>> solver('2*x + 1 = x')
        'x = -1.000000'
    
    Il secondo argomento, che per default vale 'x', consente di specificare la variabile:

        >>> solver('2*y + 1 = y', var='y')
        'y = -1.000000'

    Nel caso in cui l'equazione non ammetta una unica soluzione, la funzione lancia una
    eccezione:
    
        >>> solver('x = x')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: float division by zero
    """
    c = eval(eq.replace('=', '-(') + ')', {var: 1j}) 
    return '%s = %f' %(var, -c.real / c.imag)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
