import pulp

C = {1:18, 2:12, 3:14, 4:19, 5:11, 6:15} # 価値
A = {1:22, 2:9, 3:13, 4:24, 5:21, 6:14} # 重さ

x = {i:pulp.LpVariable(f'x{i}', cat=pulp.LpBinary) for i in C.keys()}
x

p = pulp.LpProblem('ナップサック問題', sense=pulp.LpMaximize)
p += pulp.lpSum(C[i]*x[i] for i in x.keys()), '目的関数　詰めた品物の価値'
p += pulp.lpSum(A[i]*x[i] for i in x.keys()) <= 60, '重量制約'
print(p)

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')

# ====================

xA = pulp.LpVariable('xA', 0, cat=pulp.LpInteger)
xB = pulp.LpVariable('xB', 0, cat=pulp.LpInteger)
xC = pulp.LpVariable('xC', 0, cat=pulp.LpInteger)
xD = pulp.LpVariable('xD', 0, cat=pulp.LpInteger)

p = pulp.LpProblem('資材切り出し問題', sense=pulp.LpMinimize)
p += xA + xB + xC + xD, '目的関数　各パターンで切り出した母材の本数の合計'
p += xA >= 15, '長さ70の必要部品数'
p += 2*xB + xC >= 40, '長さ40の必要部品数'
p += xC + 2*xD >= 65, '長さ28の必要部品数'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}') # 小数点以下を表示しない
