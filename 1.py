def distribute_chocolates(N):
    jar1 = 1
    if N % 2 == 0:
        jar2 = N // 2
        jar3 = N // 2
    else:
        jar2 = (N - 1) // 2
        jar3 = (N - 1) // 2 + 1
    
    return jar1, jar2, jar3

T = int(input())

for _ in range(T):
    N = int(input())
    jar1, jar2, jar3 = distribute_chocolates(N)
    print(jar1, jar2, jar3)
