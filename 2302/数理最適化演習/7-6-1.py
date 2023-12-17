import pulp

Task = ['A','B','C','D','E','F','G','T']
Time = {'A':10, 'B':6, 'C':10,'D':2, 'E':3, 'F':1, 'G':4}
Pre = {'A':[], 'B':['A'], 'C': ['A'], 'D':['B','C'], 'E':['C'],
       'F':['D'], 'G':['E','F'], 'T':['G']}
C = {'A':8, 'B':1, 'C':6, 'D':3, 'E':2, 'F':0, 'G':7}
U = {'A':3, 'B':3, 'C':4, 'D':1, 'E':1, 'F':0, 'G':3}

x = {t:pulp.LpVariable(f'x{t}') for t in Task}
s = {t:pulp.LpVariable(f's{t}', 0, U[t]) for t in Time.keys()}

p = pulp.LpProblem("最小費用による期間短縮", sense=pulp.LpMinimize)
p += (pulp.lpSum(C[t]*s[t] for t in s.keys()), "目的関数　費用")
for t in Task:
    if Pre[t] == []:
        p += x[t] >= 0, f'作業{t}は先行作業なし'
    else:
        for pre in Pre[t]:
            p += x[t] >= x[pre] + (Time[pre] - s[pre]), f'作業{t}は作業{pre}終了後に開始'
p += x['T'] <= 24, "プロジェクトを24日で完了させる"
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    if pulp.value(v) > 0:
        print(f'{v} = {pulp.value(v)}')




