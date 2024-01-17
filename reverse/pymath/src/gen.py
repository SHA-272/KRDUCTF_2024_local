import random, math

flag = "krdu{pyth0n_m4th_1mp0ss1bl3}"

for i in range(len(flag)):
    ints = [random.randint(-100, 100) for _ in range(random.randint(5, 10))]
    pos = random.randint(2, len(ints) - 1)

    ints_a = ints.copy()  # Use copy to avoid modifying the original list
    ints_a.insert(pos, ord(flag[i]))
    ans = sum(ints_a)

    s = f"{ints[0]}"
    for j in range(1, len(ints)):  # Use ints_a instead of ints to reflect the changes
        if j == pos:
            s += f"+ord(x[{i}])"
        if ints[j] >= 0:
            s += "+"
        s += f"{ints[j]}"
    s += f"!={ans}"
    print("if " + s + ": exit(1)")
