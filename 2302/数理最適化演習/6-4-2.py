import pulp

V = [1,2,3,4,5,6]
E = [(1,2), (1,3), (2,4), (2,5), (3,4), (3,6), (4,5), (4,6)]
C = {(1,2):5, (1,3):3, (2,4):4, (2,5):5, (3,4):3, (3,6):2, (4,5):5, (4,6):3}
U = {(1,2):20, (1,3):10, (2,4):10, (2,5):15, (3,4):10, (3,6):10, (4,5):20, (4,6):20}
B = {1:25, 2:0, 3:-10, 4:15, 5:-20, 6:-10}

x = {e:pulp.LpVariable(f'x{e[0]}_{e[1]}', lowBound=0, upBound=U[e]) for e in E}

p = pulp.LpProblem('最小費用流問題', sense=pulp.LpMinimize)
p += pulp.lpSum(C[e]*x[e] for e in E), '目的関数　輸送コスト'
# 流量保存制約
for i in V:
    inflow = []
    outflow = []
    for e in E:
        if e[1] == i:
            inflow.append(e)
        if e[0] == i:
            outflow.append(e)
    net_outflow = pulp.lpSum(x[e] for e in outflow) - pulp.lpSum(x[e] for e in inflow)
    p += net_outflow == B[i], f'点{i}'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')





