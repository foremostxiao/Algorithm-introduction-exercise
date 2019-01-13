# 4. 使用至少一种算法解决迷宫寻路问题。

# 学了两种方法解决迷宫问题
# 1 栈   先进后出  --深度优先
# 2 队列  先进先出    ---广度优先

# 使用栈
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]
# 起点：(x1,y1)；终点：(x2,y2)
def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack)>0):
        curNode = stack[-1] # 当前的节点
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点了
            for p in stack:
                print(p)
            return True

        # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1
        # 得出结论：for 循环正常执行结束后，else 语句里面的内容也会正常执行。
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                # 已经走过的标记一下
                maze[nextNode[0]][nextNode[1]] = 2 # 2表示为已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False
# (1,1)为0  (8,8)为0 -对角线
maze_path(1,1,8,8)



