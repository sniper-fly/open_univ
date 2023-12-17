import pulp

Task = ['A','B','C','D','E','F','G']

x = {i+1:pulp.LpVariable(f'x{i+1}') for i in range(7)}
d = {j:pulp.LpVariable(f'd{j}',0,0.001) for j in Task}

p = pulp.LpProblem('クリティカルパス(AOA)', sense=pulp.LpMaximize)
p += pulp.lpSum(d[j] for j in Task), '目的関数　作業遅延の総和'
p += x[1] >= 0, '点1'
p += x[2] >= x[1] + (10+d['A']), '点2'
p += x[3] >= x[2] + (10+d['C']), '点3'
p += x[4] >= x[2] + (6+d['B']), '点4-1'
p += x[4] >= x[3], '点4-2'
p += x[5] >= x[4] + (2+d['D']), '点5'
p += x[6] >= x[3] + (3+d['E']), '点6-1'
p += x[6] >= x[5] + (1+d['F']), '点6-2'
p += x[7] >= x[6] + (4+d['G']), '点7'
p += x[7] <= 27, 'プロジェクト完了は最早完了時刻の27から遅延しない'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')

