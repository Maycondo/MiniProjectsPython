


def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)# Factorial function in Python # Funcao fatorial em Python
    

# Example usage
print(fat(5))  # Output: 120