import pulp

x1 = pulp.LpVariable("x1", 0) # 決定変数 x1 >= 0
x2 = pulp.LpVariable("x2", 0) # 決定変数 x2 >= 0

p = pulp.LpProblem("生産計画問題", sense=pulp.LpMaximize) # 目的関数を最大化
p += (x1 + 4*x2, "目的関数　利益見込み")
p += (x1 + 3*x2 <= 24, "原料制約")
p += (4*x1 + 4*x2 <= 48, "労働時間制約")
p += (2*x1 + x2 <= 22, "機械稼働制約")
p

result = p.solve()
pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')

# 決定変数の値と限界コスト    
for v in p.variables():
    print(f'{v} = {pulp.value(v):10}, Reduced cost = {v.dj}')

# 潜在価格と余裕
for cname, c in list(p.constraints.items()):
    print(f'{cname:6s}, Shadow price = {c.pi:6}, Slack = {c.slack}')


