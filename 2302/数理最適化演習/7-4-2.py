import pulp

Task = ['A','B','C','D','E','F','G','T']
Time = {'A':10, 'B':6, 'C':10,'D':2, 'E':3, 'F':1, 'G':4}
Pre = {'A':[], 'B':['A'], 'C': ['A'], 'D':['B','C'], 'E':['C'],
       'F':['D'], 'G':['E','F'], 'T':['G']}

x = {t:pulp.LpVariable(f'x{t}') for t in Task}
d = {t:pulp.LpVariable(f'd{t}', 0, 0.001) for t in Time.keys()}

p = pulp.LpProblem('クリティカルパス', sense=pulp.LpMaximize)
p += pulp.lpSum(d), '目的関数　最早完了時刻問題'
for t in Task:
    if Pre[t] == []:
        p += x[t] >= 0, f'作業{t}は先行作業なし'
    else:
        for pre in Pre[t]:
            p += x[t] >= x[pre] + (Time[pre] + d[pre]), f'作業{t}は作業{pre}終了後に開始'
p += x['T'] <= 27, 'プロジェクトは延長しない'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')


# 別の定式化
x2 = {t:pulp.LpVariable(f'x{t}', 0) for t in Task}
d2 = {t:pulp.LpVariable(f'd{t}', cat=pulp.LpBinary) for t in Time.keys()}

p2 = pulp.LpProblem('クリティカルパス', sense=pulp.LpMaximize)
p2 += pulp.lpSum(d2), '目的関数　最早完了時刻問題'
for t in Task:
    if Pre[t] == []:
        p2 += x2[t] >= 0, f'作業{t}は先行作業なし'
    else:
        for pre in Pre[t]:
            p2 += x2[t] >= x2[pre] + (Time[pre] + 0.001*d2[pre]), f'作業{t}は作業{pre}終了後に開始'
p2 += x2['T'] <= 27, 'プロジェクトは延長しない'
p2


result2 = p2.solve()

pulp.LpStatus[result2]
pulp.value(p2.objective)
for v in p2.variables():
    print(f'{v} = {pulp.value(v)}')
