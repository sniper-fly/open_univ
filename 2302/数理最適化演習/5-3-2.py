import pulp

V = [i+1 for i in range(6)]
E = [(1,2), (1,3), (2,1), (2,3), (2,4), (3,1), (3,2), (3,5), (4,3), (4,6), (5,3), (5,6)]
W = {(1,2):1, (1,3):5, (2,1):1, (2,3):2, (2,4):2,
    (3,1):5, (3,2):4, (3,5):2, (4,3):3, (4,6):3, (5,3):1, (5,6):4}
s = 1
t = 5

x = {e:pulp.LpVariable(f'x{e[0]}_{e[1]}', cat=pulp.LpBinary) for e in E}

p = pulp.LpProblem('最短路問題', sense=pulp.LpMinimize)
p += pulp.lpSum(W[e]*x[e] for e in E), '目的関数　経路長'
for i in V:
    inflow = []
    outflow = []
    for e in E:
        if e[1] == i:
            inflow.append(e)
        if e[0] == i:
            outflow.append(e)
    net_outflow = pulp.lpSum(x[e] for e in outflow) - pulp.lpSum(x[e] for e in inflow)
    if i == s:
        p += net_outflow == 1, f'始点{i}'
    elif i == t:
        p += net_outflow == -1, f'終点{i}'
    else:
        p += net_outflow == 0, f'中間点{i}'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f'{v} = {pulp.value(v):.0f}')
