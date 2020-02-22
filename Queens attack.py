l = list(map(int, input().split(" ")));
n = l[0];
k = l[1];
qp = list(map(int, input().split(" ")));
qpn = qp[0];
qpk = qp[1];
obs = [list(map(int, input().split(" "))) for i in range(k)];


def leftdiag(qpn, qpk, obs):
    s1 = qpn;
    s2 = qpk;
    a = []
    while s1 != 1 and s2 != 1:
        s1 = s1 - 1;
        s2 = s2 - 1;
        s = [s1, s2]
        if s in obs:
            break
        else:
            a.append([s1, s2])  # left diagonal right side
    s1 = qpn;
    s2 = qpk;
    while s1 != n and s2 != n:
        s1 = s1 + 1;
        s2 = s2 + 1;
        if [s1, s2] in obs:
            break;

        else:
            a.append([s1, s2])  # left diagonla right side
    s1 = qpn;
    s2 = qpk;
    while s1 != n and s2 != 1:
        s1 = s1 + 1;
        s2 = s2 - 1;
        if [s1, s2] in obs:
            break;
        else:
            a.append([s1, s2])  # right diagonal left side
    s1 = qpn;
    s2 = qpk;
    while s1 != 1 and s2 != n:
        s1 = s1 - 1;
        s2 = s2 + 1;
        if [s1, s2] in obs:
            break;
        else:
            a.append([s1, s2])  # right diagonal right side
    s1 = qpn;
    s2 = qpk;
    while s2 != n:
        s2 = s2 + 1;  # upper column side
        if [s1, s2] in obs:
            break;
        else:
            a.append([s1, s2])
    s1 = qpn;
    s2 = qpk;
    while s2 != 1:
        s2 = s2 - 1;
        if [s1, s2] in obs:
            break;  # lower column side
        else:
            a.append([s1, s2])
    s1 = qpn;
    s2 = qpk;
    while s1 != n:
        s1 = s1 + 1
        if [s1, s2] in obs:
            break;
        else:
            a.append([s1, s2])  # upper row side
    s1 = qpn;
    s2 = qpk;
    while s1 != 1:
        s1 = s1 - 1;
        if [s1, s2] in obs:
            break;

        else:
            a.append([s1, s2])  # lower row side

    return len(a)


print(leftdiag(qpn, qpk, obs))