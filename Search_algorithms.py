from queue import PriorityQueue 
def minim(curr,heuristic):
    ind=0
    f=float('inf')
    for i in curr:
        cind=curr.index(i)
        fc=i[0]+heuristic[i[1][-1]]
        if fc<=f:
            f=fc
            ind=cind
    return ind

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
    explored = [start_point]
    nodes = []
    for i in range(1,len(Cost[start_point])):
        if (Cost[start_point][i] > 0):
            nodes.append(i)
    for node in nodes:
        cost = Cost[start_point][node]
        path = [start_point,node]
        frontier.put((cost,path))
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
          
def DFS_Traversal(cost,start_point,goals,vis,stack):
    neighbour=[]
    if len(stack)>0:
        node=stack.pop()
    if node not in vis:
        vis.append(node)
    if node in goals:
        if cost[vis[-2]][node]>0:
            return vis
        else:
            vis.remove(vis[-2])
            return vis
    else:
        for i in range(1,len(cost[start_point])):
            if(cost[start_point][i]>0):
                neighbour.append(i)
        neighbour.sort(reverse=True)
        for j in neighbour:
            if j not in vis:
                stack.append(j)
        start=stack[-1]	
        DFS_Traversal(cost,start,goals,vis,stack)
    return vis



'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

'''

def tri_traversal(cost, heuristic, start_point, goals):
    vis=[]
    stack=[start_point]
    l = []
    t1 = DFS_Traversal(cost,start_point,goals,vis,stack)
    t2 = UCS_Traversal(cost,start_point,goals)
    t3 = A_star_Traversal(
    cost, heuristic, start_point, goals 
)
    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
