import pulp

S = [1,2] # 送出元の番号
D = [1,2,3] # 受取先の番号
C = {(1,1):10, (1,2):6, (1,3):16, (2,1):8, (2,2):8, (2,3):10} # 輸送コスト
Supply = {1:100, 2:180} # 送出元の送出可能量
Demand = {1:120, 2:40, 3:80} # 受取先の受取量

x ={(i,j):pulp.LpVariable(f'x{i}_{j}',0) for i in S for j in D}
x

p = pulp.LpProblem('輸送問題', sense=pulp.LpMinimize)
p += pulp.lpSum(C[(i,j)]*x[(i,j)] for i in S for j in D), '目的関数　輸送コスト'
for i in S:
    p += pulp.lpSum(x[(i,j)] for j in D) <= Supply[i], f'送出元{i}の送出可能量制約'
for j in D:
    p += pulp.lpSum(x[(i,j)] for i in S) == Demand[j] , f'受取先{j}の受取量制約'
p

result = p.solve()

pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')
