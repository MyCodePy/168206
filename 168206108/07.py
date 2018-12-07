sta = 'hit'
end = 'cog'
alist = ['hot','dot','dog','lot','log']
path = ['hit']
c = 0
for i in alist:
    for j in range(len(i)):
        if i[j] == sta[j]:
            c += 1
    if c == len(sta) - 1:
        path.append(i)
        sta = i
        c = 0
    if sta == end:
        break;
if __name__ == '__main__':
    path.append(end)
    print(path)
