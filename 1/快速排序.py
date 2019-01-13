# 初始列表[4,3,2,15]
# 以li[0]为基数   left==>li[0],right==>li[3]

# [6,1,2,7,9,3,4,5,10,8]
# 首先哨兵j开始出动。因为此处设置的基准数是最左边的数，所以需要让哨兵j先出动，这一点非常重要。
#
# 哨兵j一步一步地向左挪动（即j--），直到找到一个小于6的数停下来。接下来哨兵i再一步一步向右挪动（即i++），直到找到一个数大于6的数停下来。
#
# 最后哨兵j停在了数字5面前，哨兵i停在了数字7面前。
# # 时间复杂度 O(nlogn)  最坏时间复杂度 O(n^2)


def parition(li,left,right):
    tmp = li[left]
    while left<right:
        while left<right and li[right]>=tmp:#先从右边找比基数小的数
            right -=1
        li[left] = li[right]
        while left<right and li[left]<=tmp:
            left +=1
        li[right] = li[left]
    # left和right碰头了 tmp归位
    li[left] = tmp
    return left

def quick_sort(li,left,right):
    if left<right:
        mid = parition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)
import random
li = [i for i in range(100)]
random.shuffle(li)
quick_sort(li,0,len(li)-1)
print(li)
