from queue import PriorityQueue 

def A_star_Traversal(cost, heuristic, start_point, goals):
    finalpath = []
    curr=PriorityQueue()
    s=[start_point]
    curr.put((heuristic[start_point],0,s))
    visit=[]
    for i in range(0,len(heuristic)):
        visit.append(0)
    while not curr.empty():
        f,g,s=curr.get()
        node=s[-1]
        if node in goals:
            finalpath=s
            break
        else:
            if visit[node]==0:
                visit[node]=1
                for u in range(1,len(heuristic)):
                    if (cost[node][u] >0):
                        gn=g+cost[node][u] 
                        f=gn+heuristic[u]
                        curr.put((f,gn,s+[u]))                  
    return finalpath


def UCS_Traversal(Cost,start_point,goals):
    goal_path = []
    explored = []
    frontier = PriorityQueue()
    start = [start_point]
    frontier.put((0,start))
    while not frontier.empty():
        path_cost,path = frontier.get()
        active_node = path[-1]
        if active_node in goals:
            goal_path = path
            break 
        if active_node not in explored:
            explored.append(active_node) 
            child_nodes=[] 
            for i in range(1,len(Cost[active_node])):
                if (Cost[active_node][i] > 0):
                    child_nodes.append(i)
            for child_node in child_nodes:
                Path_cost = Cost[active_node][child_node] + path_cost
                node = [child_node]
                Path = path + node
                frontier.put((Path_cost,Path))   
    return goal_path


def DFS_Traversal(cost,start_point,goals):
    vis=[]
    stack=[{start_point:[start_point]}]
    while stack:
        neighbour=[]
        node=list(stack[-1].keys())[0]
        path=stack[-1][node]
        stack.pop()
        if node not in vis:
            vis.append(node)
        if node in goals:
            return path
        for i in range(1,len(cost[node])):
            if(cost[node][i]>0):
                neighbour.append(i)
        neighbour.sort(reverse=True)
        child_path=[]
        for j in neighbour:
            if j not in vis:
                child_path=path+[j]
                stack.append({j:child_path})
    return []

def tri_traversal(cost, heuristic, start_point, goals):
    l = []
    t1 = DFS_Traversal(cost,start_point,goals)
    t2 = UCS_Traversal(cost,start_point,goals)
    t3 = A_star_Traversal(cost, heuristic, start_point, goals)
    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l

