import pulp

blank = -1000
Actor = [i + 1 for i in range(5)]
Role = [j + 1 for j in range(5)]
C = {
    (1, 1): 5,
    (1, 2): blank,
    (1, 3): 1,
    (1, 4): blank,
    (1, 5): blank,
    (2, 1): blank,
    (2, 2): 2,
    (2, 3): blank,
    (2, 4): 8,
    (2, 5): 7,
    (3, 1): 4,
    (3, 2): blank,
    (3, 3): 6,
    (3, 4): 7,
    (3, 5): blank,
    (4, 1): blank,
    (4, 2): blank,
    (4, 3): 9,
    (4, 4): blank,
    (4, 5): 4,
    (5, 1): 7,
    (5, 2): 8,
    (5, 3): blank,
    (5, 4): blank,
    (5, 5): 6,
}

x = {
    (i, j): pulp.LpVariable(f"x{i}_{j}", cat=pulp.LpBinary) for i in Actor for j in Role
}

p = pulp.LpProblem("割り当て問題", sense=pulp.LpMaximize)
p += pulp.lpSum(C[(i, j)] * x[(i, j)] for i in Actor for j in Role), "目的関数　配役の評価値"
for i in Actor:
    p += pulp.lpSum(x[(i, j)] for j in Role) == 1, f"俳優{i}は一役を演じる制約"
for j in Role:
    p += pulp.lpSum(x[(i, j)] for i in Actor) == 1, f"役{j}は一俳優が演じる制約"
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f"{v} = {pulp.value(v):.0f}")
