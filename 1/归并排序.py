# 基本思想：先分解再合并
# 二分 将列表越分越小，直到分成一个元素
# 终止条件：一个元素是有序的
# 合并 需要一个专门的列表来存储排好序的元素
# 时间复杂度 O(nlogn)
def merge(li,low,mid,high):
    i = low
    j = mid+1
    ltmp = []
    # 左边 中间  右边
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i +=1
        else:
            ltmp.append(li[j])
            j +=1

    # 把剩余较大的加入列表
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
        j+=1
    # 切片不包括结束位置的索引
    li[low:high+1]=ltmp
def merge_sort(li,low,high):
    if low<high:#至少有两个元素
        # 二分
        mid = (low+high)//2
        # 右边递归完
        merge_sort(li,mid+1,high)

        # 左边递归完
        merge_sort(li,low,mid)
        # 做归并处理
        merge(li,low,mid,high)
li = list(range(10))
import random
random.shuffle(li)
merge_sort(li,0,len(li)-1)
print(li)









