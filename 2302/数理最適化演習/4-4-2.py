import pulp

Actor = [i+1 for i in range(4)]
Role = [j+1 for j in range(4)]
C = {(1,1):3, (1,2):6, (1,3):9, (1,4):8, (2,1):6, (2,2):3, (2,3):2, (2,4):4,
     (3,1):9, (3,2):3, (3,3):2, (3,4):5, (4,1):6, (4,2):2, (4,3):3, (4,4):8}

x ={(i,j):pulp.LpVariable(f'x{i}_{j}', cat=pulp.LpBinary) for i in Actor for j in Role}

p = pulp.LpProblem('割り当て問題', sense=pulp.LpMaximize)
p += pulp.lpSum(C[(i,j)]*x[(i,j)] for i in Actor for j in Role), '目的関数　配役の評価値'
for i in Actor:
    p += pulp.lpSum(x[(i,j)] for j in Role) == 1, f'俳優{i}は一役を演じる制約'
for j in Role:
    p += pulp.lpSum(x[(i,j)] for i in Actor) == 1, f'役{j}は一俳優が演じる制約'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f'{v} = {pulp.value(v):.0f}')
