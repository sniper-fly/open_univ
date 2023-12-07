import pulp

C = {1:9, 2:7, 3:6, 4:5, 5:3} # 価値
A = {1:6, 2:4, 3:5, 4:3, 5:3} # 重さ

x = {i:pulp.LpVariable(f'x{i}', cat=pulp.LpBinary) for i in C.keys()}
x

p = pulp.LpProblem('ナップサック問題', sense=pulp.LpMaximize)
p += pulp.lpSum(C[i]*x[i] for i in x.keys()), '目的関数　詰めた品物の価値'
p += pulp.lpSum(A[i]*x[i] for i in x.keys()) <= 17, '重量制約'
print(p)

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')
