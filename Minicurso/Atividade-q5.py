def fatorial(a):
    if a == 1:
        return 1

    return a * fatorial(a-1)

print("Digite o número")
n = int(input())

print(fatorial(n))
