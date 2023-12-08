S = [1, 2, 3]  # 送出元の番号
D = [1, 2]  # 受取先の番号
C = {(1, 1): 16, (1, 2): 8, (2, 1): 10, (2, 2): 16, (3, 1): 12, (3, 2): 14}  # 輸送コスト
Supply = {1: 120, 2: 100, 3: 80}  # 送出元の送出可能量
Demand = {1: 160, 2: 140}  # 受取先の受取量

x = {(i, j): pulp.LpVariable(f"x{i}_{j}", 0) for i in S for j in D}
x

p = pulp.LpProblem("輸送問題", sense=pulp.LpMinimize)
p += pulp.lpSum(C[(i, j)] * x[(i, j)] for i in S for j in D), "目的関数　輸送コスト"
for i in S:
    p += pulp.lpSum(x[(i, j)] for j in D) <= Supply[i], f"送出元{i}の送出可能量制約"
for j in D:
    p += pulp.lpSum(x[(i, j)] for i in S) == Demand[j], f"受取先{j}の受取量制約"
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")

# ========================================

Actor = [i + 1 for i in range(4)]
Role = [j + 1 for j in range(4)]
C = {
    (1, 1): 5,
    (1, 2): 0,
    (1, 3): 3,
    (1, 4): 2,
    (2, 1): 5,
    (2, 2): 4,
    (2, 3): 2,
    (2, 4): 0,
    (3, 1): 0,
    (3, 2): 2,
    (3, 3): 0,
    (3, 4): 4,
    (4, 1): 0,
    (4, 2): 2,
    (4, 3): 5,
    (4, 4): 0
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
