import pulp

Task = ["A", "B", "C", "D", "E", "F", "T"]
Time = {"A": 10, "B": 7, "C": 4, "D": 8, "E": 3, "F": 4}
Pre = {
    "A": [],
    "B": [],
    "C": ["A", "B"],
    "D": ["A", "B"],
    "E": ["C"],
    "F": ["D", "E"],
    "T": ["F"],
}

x = {t: pulp.LpVariable(f"x{t}") for t in Task}

p = pulp.LpProblem("最早完了時刻", sense=pulp.LpMinimize)
p += x["T"], "目的関数　Tの開始時刻"
for t in Task:
    if Pre[t] == []:
        p += x[t] >= 0, f"作業{t}は先行作業なし"
    else:
        for pre in Pre[t]:
            p += x[t] >= x[pre] + Time[pre], f"作業{t}は作業{pre}終了後に開始"
p

result = p.solve()
pulp.LpStatus[result]
pulp.value(p.objective)
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")
