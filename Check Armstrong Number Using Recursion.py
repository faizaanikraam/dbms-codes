n = 153
p = len(str(n))

def arm(x):
    if x == 0:
        return 0
    return (x % 10) ** p + arm(x // 10)

if arm(n) == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")