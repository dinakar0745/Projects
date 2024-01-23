t = int(input())

for i in range(t):
    a, b, c, d, e, f = input().split()

    if (a == 'W' and b == 'W' and c == 'W') or (b == 'W' and c == 'W' and d == 'W') or (c == 'W' and d == 'W' and e == 'W') or (d == 'W' and e == 'W' and f == 'W'):
        print("YES")
    else:
        print("NO")
