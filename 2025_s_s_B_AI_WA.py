dot = 0
N = int(input().strip())
Q = list(map(int, input().strip().split()))
C = list(map(int, input().strip().split()))
A, B = map(int, input().strip().split())

for i in range(N):
    D_i = (C[i] * (B - A)) // 255 + A
    dot += Q[i] * D_i

print(dot)
