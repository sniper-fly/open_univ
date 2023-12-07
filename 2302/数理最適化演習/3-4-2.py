import pulp

xA = pulp.LpVariable('xA', 0, cat=pulp.LpInteger)
xB = pulp.LpVariable('xB', 0, cat=pulp.LpInteger)
xC = pulp.LpVariable('xC', 0, cat=pulp.LpInteger)
xD = pulp.LpVariable('xD', 0, cat=pulp.LpInteger)

p = pulp.LpProblem('資材切り出し問題', sense=pulp.LpMinimize)
p += xA + xB + xC + xD, '目的関数　各パターンで切り出した母材の本数の合計'
p += xA >= 12, '長さ70の必要部品数'
p += 2*xB + xC >= 34, '長さ40の必要部品数'
p += xA + 2*xC + 3*xD >= 62, '長さ28の必要部品数'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}') # 小数点以下を表示しない

