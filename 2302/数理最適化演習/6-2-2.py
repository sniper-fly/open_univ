import pulp

V = [i+1 for i in range(7)]
E = [(1,2), (1,3), (2,1), (2,4), (2,5), (3,4), (3,6), (4,7), (5,7), (6,7), (7,4)]
U = {(1,2):3, (1,3):5, (2,1):5, (2,4):2, (2,5):2, (3,4):3, (3,6):3,
     (4,7):2, (5,7):3, (6,7):4, (7,4):3}
s = 1
t = 7

x = {e:pulp.LpVariable(f'x{e[0]}_{e[1]}', lowBound=0, upBound=U[e])
     for e in E} # upBound=U[e] 容量制約
z = pulp.LpVariable('z')

p = pulp.LpProblem('最大流問題', sense=pulp.LpMaximize)
p += z, '目的関数　流量'
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
        p += net_outflow == z, f'始点{i}'
    elif i == t:
        p += net_outflow == -z, f'終点{i}'
    else:
        p += net_outflow == 0, f'点{i}'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f'{v} = {pulp.value(v)}')
