# 基本思想
# 将指定的排序位置与其他元素进行对比，如果满足条件就交换元素值，把满足条件的元素与指定的排序位置交换
# 每一次循环选出最小的元素
# 外层循环n-1次
# 时间复杂度 O(n^2)
def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j] = li[j],li[i]
li = [3,2,4,1,5,6,8,7,9]
select_sort(li)
print(li)