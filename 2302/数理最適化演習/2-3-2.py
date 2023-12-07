import pulp

x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)

p = pulp.LpProblem("食事問題", sense=pulp.LpMinimize)
p += 12 * x1 + 15 * x2, "目的関数　価格"
p += 3 * x1 + 2 * x2 >= 200, "栄養素1の必要摂取量"
p += x1 + 5 * x2 >= 160, "栄養素2の必要摂取量"
p += 4 * x1 + 3 * x2 >= 250, "栄養素3の必要摂取量"
p

result = p.solve()

print(pulp.LpStatus[result])
print(pulp.value(p.objective))
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")

# /////////

xA = pulp.LpVariable("xA", 0)
xB = pulp.LpVariable("xB", 0)
xC = pulp.LpVariable("xC", 0)

p = pulp.LpProblem("食事問題", sense=pulp.LpMinimize)
p += 75 * xA + 62 * xB + 50 * xC, "目的関数　価格"
p += 30 * xA + 18 * xB + 11 * xC >= 150, "栄養素1の必要摂取量"
p += 18 * xA + 22 * xB + 40 * xC >= 100, "栄養素2の必要摂取量"
p += 2 * xA + 3 * xB + 5 * xC >= 15, "栄養素3の必要摂取量"
print(p)

result = p.solve()

print(pulp.LpStatus[result])
print(pulp.value(p.objective))
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")

# /////////

x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)

p = pulp.LpProblem("食事問題", sense=pulp.LpMaximize)
p += 4 * x1 + 3 * x2, "目的関数　価格"
p += 5 * x1 + 2 * x2 <= 50, "栄養素1の必要摂取量"
p += x1 + x2 <= 20, "栄養素2の必要摂取量"
p += 4 * x1 + 5 * x2 <= 90, "栄養素3の必要摂取量"
p

result = p.solve()

print(pulp.LpStatus[result])
print(pulp.value(p.objective))
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")

# ////////

x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)

p = pulp.LpProblem("食事問題", sense=pulp.LpMinimize)
p += 9 * x1 + 6 * x2, "目的関数　価格"
p += 8 * x1 + 5 * x2 >= 1300, "栄養素1の必要摂取量"
p += 2 * x1 + 3 * x2 >= 500, "栄養素2の必要摂取量"
p

result = p.solve()

print(pulp.LpStatus[result])
print(pulp.value(p.objective))
for v in p.variables():
    print(f"{v} = {pulp.value(v)}")
