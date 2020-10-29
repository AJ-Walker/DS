def hanoi(n, P1, P2, P3):
    if n == 0:
        return

    global count
    count += 1
    hanoi(n-1, P1, P3, P2)

    if P1:
        P3.append(P1.pop())
        print(f"Pole 1 : {A}, Pole 2 : {B}, Pole 3 : {C}\n")

    hanoi(n-1, P2, P1, P3)

n = 3
A = list(range(n,0,-1))
B, C = [], []
print(f"{A[0]} is big disc, {A[1]} is medium disc, {A[2]} is small disc.")
print(f"Pole 1 : {A}, Pole 2 : {B}, Pole 3 : {C}\n")
count = 0
hanoi(n, A, B, C)
print(f"Total Steps : {count}")