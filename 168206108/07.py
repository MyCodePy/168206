# -*- coding: utf-8 -*-
sta = 'hit'

end = 'cog'

alist = ['hiqa','hot','dpc','dot','dog','aog','lop','loc','log']

path = ['hit']#初始化一个只有起点的列表

#判断两个单词是否只差一个字母
def find_r(sta_,end_):
    if len(end_) == len(sta_):
        right = 0
        for i in range(len(sta_)):
            if sta_[i] != end_[i]:
                right += 1
        if right == 1:
            return True
    return False

#添加中间路径
def find():
    global sta,alist,end
    for i in alist:
        if find_r(sta,i) == False:
            continue
        else:
            sta = i
            path.append(i)
            if find_r(sta,end):
               break;

if __name__ == '__main__':
    find()
    path.append(end)#将终点添加到列表中去
    print(path)
