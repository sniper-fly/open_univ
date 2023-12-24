import pulp

Actor = [i + 1 for i in range(4)]
Role = [j + 1 for j in range(4)]
C = {
    (1, 1): 5,
    (1, 2): 5,
    (1, 3): -100,
    (1, 4): 2,
    (2, 1): 2,
    (2, 2): 3,
    (2, 3): -100,
    (2, 4): 5,
    (3, 1): 2,
    (3, 2): -100,
    (3, 3): 5,
    (3, 4): 4,
    (4, 1): 4,
    (4, 2): -100,
    (4, 3): 5,
    (4, 4): -100,
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


Actor = [1, 2, 3]
Role = [1, 2, 3]
C = {
    (1, 1): 1,
    (1, 2): 6,
    (1, 3): 2,
    (2, 1): 2,
    (2, 2): 2,
    (2, 3): 5,
    (3, 1): -100,
    (3, 2): 4,
    (3, 3): 5,
}

x = {
    (i, j): pulp.LpVariable(f"x{i}_{j}", cat=pulp.LpBinary) for i in Actor for j in Role
}
t = pulp.LpVariable("t")

p = pulp.LpProblem("最小値版配役問題", sense=pulp.LpMaximize)
p += t, "目的関数　評価が最小の役の評価値"
for i in Actor:
    p += pulp.lpSum(x[(i, j)] for j in Role) == 1, f"俳優{i}は一役を演じる制約"
for j in Role:
    p += pulp.lpSum(x[(i, j)] for i in Actor) == 1, f"役{j}は一俳優が演じる制約"
for j in Role:
    p += pulp.lpSum(C[(i, j)] * x[(i, j)] for i in Actor) >= t, f"役{j}の評価値はt以上"
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f"{v} = {pulp.value(v):.0f}")
