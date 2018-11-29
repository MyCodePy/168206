'''Python3'''
# -*- coding: utf-8 -*-
graph = {
         "yuepu":{"haibao":0,"changpian":5},
         "haibao":{"jita":30,"jiazigu":35},
         "changpian":{"jita":15,"jiazigu":20},
         "jita":{"gangqin":20},
         "jiazigu":{"gangqin":10},
         "gangqin":{}
         }
parents = {
           "haibao":"yuepu",
           "changpian":"yuepu",
           "gangqin":None,
           "jita":None,
           "jiazigu":None
          }
costs = {
         'haibao':0,
         'changpian':5,
         'jita':float("inf"),
         'jiazigu':float("inf"),
         'gangqin':float("inf")
        }

processed = []

def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None
    for n in costs:
        cost = costs[n]
        if cost < lowest_cost and n not in processed:
            lowest_cost = cost
            lowest_cost_node = n
    return lowest_cost_node

def find_():
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs.get(node)
        for n in graph[node].keys():
            new_cost = cost + graph[node][n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
if __name__ == '__main__':
    find_()
    print("最少开销：",costs['gangqin'])
    node = 'gangqin'
    print('最少开销的路径：',end = node)
    while node is not 'yuepu':
        print(' <<< ',end = parents[node])
        node = parents[node]
