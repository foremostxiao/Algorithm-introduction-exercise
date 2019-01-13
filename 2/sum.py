# 2. 以尽可能多的方法解决2-sum问题并分析其时间复杂度：
# 给定一个列表和一个整数，从列表中找到两个数，使得两数之和等于给定的数，返回两个数的下标。题目保证有且只有一组解。
def sum(li,s):
    for i in range(0,len(li)-1):
        for j in range(i,len(li)):
            if li[i]+li[j] == s:
                return [i,j]
li = [2,4,5,8,9]
print(sum(li,9))