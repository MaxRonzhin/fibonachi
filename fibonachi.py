sequence_fib = [0, 1, 1]
def fib(n):
    if n <= len(sequence_fib)-1:
        return sequence_fib[n]
    sequence_fib.append(fib(n - 1) + fib(n - 2))
    return sequence_fib[n]
    
n = int(input ("Введите номер элемента в последовательности: "))
fib(n)